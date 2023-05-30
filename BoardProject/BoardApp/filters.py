import django_filters
from django.forms import DateTimeInput, DateInput
from django_filters import (
    FilterSet, ChoiceFilter, DateFromToRangeFilter, CharFilter, DateTimeFilter, ModelMultipleChoiceFilter,
    ModelChoiceFilter
)
from django_filters.widgets import RangeWidget

from .config.post_categories import CATEGORY_CHOICES
from .models import BoardAd


# Фильтры поиска для главной страницы
class BoardAdFilter(FilterSet):
    titleBoard = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Search table of contents",
    )

    Author = CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        label="Search by author",
    )

    dateCreation = DateFromToRangeFilter(
        field_name='dateCreation',
        lookup_expr='exact',
        label="Search by date",
        widget=RangeWidget(
            attrs={'type': 'date'}
        ),
    )

    CategoryBoard = ChoiceFilter(
        field_name='categoryBoard',
        label='',
        empty_label="Choice of category",
        choices=CATEGORY_CHOICES,
    )


# Метод для отображения статей пользователя
def title_view(request):
    if request is None:
        return BoardAd.objects.none()

    author = request.user
    return BoardAd.objects.filter(author=author)


# Фильтры поиска для личной страницы пользователя
class FeedbackFilter(FilterSet):
    titleBoard = ModelChoiceFilter(
        field_name='titleBoard',
        queryset=title_view,
        label='',
        empty_label="Title"
    )

    CategoryBoard = ChoiceFilter(
        field_name='categoryBoard',
        label='',
        choices=CATEGORY_CHOICES,
        empty_label="Clan"
    )

    dateCreation = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
