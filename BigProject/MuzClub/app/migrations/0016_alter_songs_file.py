# Generated by Django 4.1.5 on 2023-02-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_songs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='file',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
