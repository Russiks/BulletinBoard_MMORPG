from django import forms
from django.core.exceptions import ValidationError

from .models import BoardAd, Feedback


# Класс форма для создания объявления
class BoardAdForm(forms.ModelForm):
    class Meta:
        model = BoardAd
        widgets = {'titleBoard': forms.TextInput(attrs={'size': '100'})}
        fields = (
            'categoryBoard',
            'titleBoard',
            'contentBoard',
        )

    def __init__(self, *args, **kwargs):
        super(BoardAdForm, self).__init__(*args, **kwargs)
        self.fields['categoryBoard'].label = 'Category:'
        self.fields['titleBoard'].label = 'Title'
        self.fields['contentBoard'].label = 'Announcement text:'

    def clean_titleBoard(self):
        name = self.cleaned_data['titleBoard']
        if name[0].islower():
            raise ValidationError(
                "The name must begin with a capital letter"
            )
        return name


# Класс форма для создания отклика
class FeedbackForm(forms.ModelForm):
    textComment = forms.CharField(
        label='',
        widget=forms.Textarea(),
        required=True
    )

    class Meta:
        model = Feedback
        fields = ['textComment']
