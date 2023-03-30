from django.core.management.base import BaseCommand, CommandError
from app.models import Author, Category, Songs
from random import random


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        print('Deleting old data')
        Songs.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        print('End of deletings')
        #
        print('Creating new data')
        category = ['Sad', 'Happy', 'Relax']
        # # authors = ['Bilyash', 'Eminem', 'Dream']
        # # name = ['Bad Guy', 'Hi Five', 'Phonk']
        # colors = [144238144, 135206250, 240230140]
        # #
        for el in range(0, len(category)):
            cater = Category.objects.create(title=category[el])
        #     # author = Author.objects.create(username=authors[el])
        #     # song = Songs.objects.create(name=name[el], category=cater, author=author, rating=round(random()*5, 1))
        print('End of creating')
        #
        # print('Вывод всех элементов')
        # songs = Songs.objects.all()
        # print('All Songs:')
        # for song in songs:
        #     song_name = str(song.name)
        #     song_category = str(song.category.title)
        #     song_author = str(song.author.username)
        #     song_rating = str(song.rating)
        #     print('|', song_name.center(10), '|', song_category.center(10), '|', song_author.center(10), '|', song_rating.center(10), '|',)
        #
        # categories = Category.objects.all()
        # print('All Categories:')
        # for cat in categories:
        #     category_name = str(cat.title)
        #     print('|', category_name.center(10), '|')
        #
        # authors = Author.objects.all()
        # print('All Authors:')
        # for auths in authors:
        #     author_name = str(auths.username)
        #     print('|', author_name.center(10), '|')
