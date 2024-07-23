from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('cart/', CartViewApi.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contactus/', ContactViewApi.as_view(), name='contactus'),

    path('login/', LoginView.as_view(), name='login'),
    path('authenticate/', LoginViewApi.as_view(), name='authenticate'),
]