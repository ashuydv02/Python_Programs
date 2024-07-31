from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    # path('', views.api_route, name='api_root'),
    path('crud/', views.Employee_api.as_view(), name='employee_api'),
    path('crud/<int:pk>/', views.Employee_api_details.as_view()),
    path('user/', views.User_api.as_view(), name='user_api'),
    # path('crud/', views.employee_list),
    # path('crud/<int:pk>/', views.employee_detail),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token),
]   

urlpatterns = format_suffix_patterns(urlpatterns)
