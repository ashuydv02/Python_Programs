from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/', views.MyView.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='class_base_view_app/about.html'))
]
