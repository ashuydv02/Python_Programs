from django.urls import path, include
from rest_framework_nested import routers
from .views import AuthorViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author_router')

authors_router = routers.NestedDefaultRouter(router, r'authors', lookup='author')
authors_router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(authors_router.urls)),
]