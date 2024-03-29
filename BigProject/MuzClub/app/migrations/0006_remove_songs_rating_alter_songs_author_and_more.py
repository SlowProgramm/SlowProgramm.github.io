# Generated by Django 4.1.5 on 2023-02-13 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_songs_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='rating',
        ),
        migrations.AlterField(
            model_name='songs',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='songs',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.category'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
    ]
