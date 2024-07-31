from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Books
from django.contrib.auth.models import User

class ViewTest(TestCase):
    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_index(self):
        c = Client()
        url = reverse('index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")

class MyModelTest(TestCase):
    def test_book_model(self):
        user = User.objects.create(username='ay', email='ay@mail.com')
        user.save()
        book = Books.objects.create(title='book1', author=user)
        self.assertEqual(book.title, 'book1')

    def test_user_model(self):
        user = User.objects.create(username='ay', email='ay@mail.com')
        user.set_password('ay')
        user.save()
        user = User.objects.get(username='ay')
        self.assertEqual(user.username, 'ay')