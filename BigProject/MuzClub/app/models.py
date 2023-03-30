from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=24)

    def __str__(self):
        return f'{self.title}'


class Songs(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=255)
    file = models.FileField(upload_to='songs/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])], null=False, blank=False)
    author_name = models.CharField(verbose_name='author_name', max_length=64, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} song'


class Profile(models.Model):
    username = models.CharField(verbose_name='name', max_length=64, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    favors = models.ManyToManyField(Songs)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username} '
