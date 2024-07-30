from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from .models import Books


class HomeView(TemplateView):
    template_name = 'home.html'


def index(request):
    return HttpResponse("Welcome")


def books(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

