from django.test import TestCase
from .views import random_rating
from .models import Category, Author, Songs
# python manage.py test


class TestCategory(TestCase):
    def test_str(self):
        author = Author.objects.create(username='Артур Пирожков')
        self.assertEqual(str(author), 'Артур Пирожков')


class TestAuthor(TestCase):
    def test_str(self):
        category = Category.objects.create(title='Энергичная')
        self.assertEqual(str(category), 'Энергичная')


class TestSong(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(title='Энергичная')
        author = Author.objects.create(username='Артур Пирожков')
        self.rating = random_rating()
        self.song = Songs.objects.create(name='Рассвет', category=category, author=author, rating=self.rating)

    def test_str(self):
        self.assertEqual(str(self.song), f"Рассвет [Энергичная] [Артур Пирожков] [{self.rating}]")


class TestContext(TestCase):
    def test_context(self):
        response = self.client.get('/songs/')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'Помогающий текст')