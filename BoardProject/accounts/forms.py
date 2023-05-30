from django import forms
from django.contrib.auth.models import User


# Класс форма для редактирования профиль пользователя
class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


# Класс форма для отправки кода подтверждения для авторизации пользователя
class AuthCodeForm(forms.Form):
    code = forms.IntegerField(
        label="Registration code",
    )
