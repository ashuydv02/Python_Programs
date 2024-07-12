from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('login/', views.User_login.as_view(), name='login'),
    path('register/', views.User_register.as_view(), name='register'),
    path('logout/', views.User_logout.as_view(), name='logout'),
]
