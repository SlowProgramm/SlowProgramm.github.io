# Generated by Django 4.1.5 on 2023-02-22 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_songs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.songs'),
        ),
    ]