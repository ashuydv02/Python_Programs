from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('addcart/', CartViewApi.as_view(), name='addcart'),
    path('addcart/<int:id>', CartViewApi.as_view(), name='updatecart'),
    path('create_order/', OrderViewApi.as_view(), name='create_order'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contactus/', ContactViewApi.as_view(), name='contactus'),

    path('login/', LoginView.as_view(), name='login'),
    path('authenticate/', LoginViewApi.as_view(), name='authenticate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registerapi/', RegisterViewApi.as_view(), name='registerapi'),
    path('profile/', ProfileView.as_view(), name='profile'),
]