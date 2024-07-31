from django.urls import path
from . import views

urlpatterns =[
    path('crud/', views.Employee_api.as_view()),
]