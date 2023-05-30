from pprint import pprint

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin,
)
from django.http import (
    HttpResponseRedirect, HttpResponse,
)
from django.core.mail import send_mail
from django.shortcuts import (
    redirect, get_object_or_404, render,
)
from django.urls import (
    reverse_lazy, reverse,
)
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)

from .filters import (
    BoardAdFilter, FeedbackFilter,
)
from .forms import (
    BoardAdForm, FeedbackForm,
)
from .models import (
    BoardAd, Feedback,
)
from .tasks import send_mail_task


# Класс-представление для отображения списка объявлений
class BoardList(ListView):
    model = BoardAd
    template_name = 'BoardApp/ad_list.html'
    context_object_name = 'ads'
    ordering = '-dateCreation', '-timeCreation'
    paginate_by = 4
    paginate_orphans = 1  # Задаем кол-во отображаемых объектов на сл. странице. Если объектов меньше или равно
    # указанной сумме в переменной, то объекты будут перенесены на предыдущею страницу

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BoardAdFilter(self.request.GET, queryset)
        # pprint(queryset)
        return self.filterset.qs  # Возвращаем отфильтрованный список

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['launch_text'] = ('New ads are always shown first!!!')
        # pprint(context)
        context['filterset'] = self.filterset
        return context


# Класс-представление для отображения деталей объявления
class BoardDetail(DetailView):
    model = BoardAd
    template_name = 'BoardApp/ad_detail.html'
    context_object_name = 'ad'


# Класс-представление для создания объявления
class BoardCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = BoardAdForm
    model = BoardAd
    template_name = 'BoardApp/ad_create.html'
    permission_required = 'BoardApp.add_boardad'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('BoardApp.add_boardad'):
            return HttpResponseRedirect(reverse('account_profile'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pprint(context)
        return context

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return redirect(f'/ads/{ad.id}')


# Класс-представление для редактирования объявления
class BoardEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = BoardAdForm
    model = BoardAd
    template_name = 'BoardApp/ad_edit.html'
    # success_url = reverse_lazy('board_detail')
    permission_required = ('BoardApp.change_boardad',)

    def get_success_url(self):
        return reverse('board_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        author = BoardAd.objects.get(pk=self.kwargs.get('pk')).author.username
        if self.request.user.username == 'russiks' or self.request.user.username == author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Warning: only the author of the ad can edit it')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return BoardAd.objects.get(pk=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/ads/' + str(self.kwargs.get('pk')))


# Класс-представление для удаления объявления
class BoardDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = BoardAd
    context_object_name = 'ad'  # Без определения context_object_name в HTML-шаблоне не выводится переменная {{ object.name }}
    template_name = 'BoardApp/ad_delete.html'
    success_url = reverse_lazy('board_list')
    permission_required = 'BoardApp.delete_boardad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['question'] = 'Are you sure you want to delete this ad?'
        return context

    def dispatch(self, request, *args, **kwargs):
        author = BoardAd.objects.get(pk=self.kwargs.get('pk')).author.username
        if self.request.user.username == 'russiks' or self.request.user.username == author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Warning: only the author of the ad can delete it')


# Класс-представление для отображения отзывов пользователю
class FeedbackList(ListView):
    model = BoardAd
    template_name = 'BoardApp/feed_list.html'
    context_object_name = 'profile'
    ordering = ['-dateCreation']
    paginate_by = 2
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FeedbackFilter(self.request.GET, request=self.request,
                                        queryset=queryset.filter(author=self.request.user))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        # pprint(self.filterset)
        # pprint(self.filterset.qs)
        return context


# Класс-представление для отображения деталей отзывов
class FeedbackDetail(DetailView):
    model = Feedback
    template_name = 'BoardApp/feed_detail.html'
    context_object_name = 'feed'
    ordering = ['-dateCreation']

    def get_object(self, queryset=None):
        comment = get_object_or_404(BoardAd, id=self.kwargs['pk'])
        response = get_object_or_404(Feedback, id=self.kwargs['pk_feed'], commentBoard=comment)
        return response


# Класс-представление для создания откликов
class FeedbackCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = FeedbackForm
    model = Feedback
    template_name = 'BoardApp/feed_create.html'
    permission_required = 'BoardApp.add_feedback'

    def get_success_url(self):
        comment_id = self.kwargs['pk']
        return reverse('board_detail', kwargs={'pk': comment_id})

    def form_valid(self, form):
        form.instance.commentBoard_id = self.kwargs['pk']
        form.instance.author = self.request.user

        ad = BoardAd.objects.get(pk=self.kwargs['pk'])

        subject = 'A new response to the ad'
        message = f"Your ad \"{ad.titleBoard}\" has received a new response."
        email = ad.author.email
        send_mail_task.delay(subject, message, email)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previous_url = self.request.META.get('HTTP_REFERER')
        context['previous_url'] = previous_url
        return context


# Класс-представление для удаления откликов на объявления
class FeedbackDelete(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = 'BoardApp/feed_delete.html'
    # success_url = reverse_lazy('board_list')

    def get_success_url(self):
        comment_id = self.kwargs['pk']
        return reverse('board_detail', kwargs={'pk': comment_id})

    def dispatch(self, request, *args, **kwargs):
        author = BoardAd.objects.get(pk=self.kwargs.get('pk')).author.username
        if self.request.user.username == 'russiks' or self.request.user.username == author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Warning: only the author of the ad can delete the response')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['question2'] = 'Are you sure you want to delete this feedback?'
        return context

    def get_object(self, queryset=None):
        comment = get_object_or_404(BoardAd, id=self.kwargs['pk'])
        response = get_object_or_404(Feedback, id=self.kwargs['pk_feed'], commentBoard=comment)
        return response


# Функциональное представление, которое принимает отклики и отправляет сообщение о данной операции
def feedback_activ(request, pk, pk_feed):
    comment = get_object_or_404(BoardAd, id=pk)
    response = get_object_or_404(Feedback, id=pk_feed, commentBoard=comment)

    text = response.textComment
    response.confirmComment = True
    response.save()
    previous_url = request.META.get('HTTP_REFERER')

    subject = f'On the ad \"{comment.titleBoard}\"'
    message = f"Your response \"{text}\" has been accepted!"
    email = response.author.email
    send_mail_task.delay(subject, message, email)

    return render(request, 'BoardApp/feed_active.html', {'text': text, 'previous_url': previous_url})


# Функциональное представление, которое отклоняет отклики и отправляет сообщение о данной операции
def feedback_deactive(request, pk, pk_feed):
    comment = get_object_or_404(BoardAd, id=pk)
    response = get_object_or_404(Feedback, id=pk_feed, commentBoard=comment)

    text = response.textComment
    response.confirmComment = False
    response.save()
    previous_url = request.META.get('HTTP_REFERER')

    subject = f'On the ad \"{comment.titleBoard}\"'
    message = f"Your response \"{text}\" has been rejected"
    email = response.author.email
    send_mail_task.delay(subject, message, email)

    return render(request, 'BoardApp/feed_deactive.html', {'text': text, 'previous_url': previous_url})
