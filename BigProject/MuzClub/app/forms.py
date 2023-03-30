from django.forms import ModelForm
from django import forms
from app.models import Songs, Profile, Category


class SongCreationForm(ModelForm):
    name = forms.CharField(help_text='', label="Название песни")
    category = forms.ModelChoiceField(label="Жанр", queryset=Category.objects.all())
    image = forms.ImageField(label="Обложка")
    file = forms.FileField(label="Файл")

    class Meta:
        model = Songs
        fields = ['name', 'category', 'image', 'file']



