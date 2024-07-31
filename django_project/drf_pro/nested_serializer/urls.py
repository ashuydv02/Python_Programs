from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookView.as_view(), name='books'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('caching/', views.CachedDataView.as_view()),
]