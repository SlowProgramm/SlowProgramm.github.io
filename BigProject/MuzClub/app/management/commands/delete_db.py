from django.core.management.base import BaseCommand, CommandError
from app.models import Author, Category, Songs


class Command(BaseCommand):
    help = 'Delete db'

    def handle(self, *args, **options):
        print('Deleting old data')
        Songs.objects.all().delete()
        Category.objects.all().delete()

