from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListSerializerView.as_view(), name='list'),
    path('score/', views.ScoreView.as_view(), name="score")
]
