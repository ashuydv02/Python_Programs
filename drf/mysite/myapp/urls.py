from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('cart/', views.CartView.as_view(), name='cart'),

    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('change_password/', views.UserChangePassword.as_view(), name='change_password'),
]
