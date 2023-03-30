from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    username = forms.CharField(help_text='', label="Имя пользователя")
    password1 = forms.CharField(help_text='', widget=forms.PasswordInput(), label="Пароль")
    password2 = forms.CharField(help_text='', widget=forms.PasswordInput(), label="Подтверждение пароля")

    class Meta:
        model = User
        fields = ('username', 'password1')


