from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', ProductViewDetails.as_view()),

    path('cart/', CartView.as_view()),
    path('cart/<int:pk>/', CartViewDetails.as_view()),

    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderViewDetails.as_view()),

    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryViewDetails.as_view()),

    path('contactus/', ContactusView.as_view()),
    path('contactus/<int:id>', ContactusViewDetails.as_view()),

    path('user/', UserView.as_view()),
]
