from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import BookSerializer
from .models import Books
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BookView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'author', 'price']
    ordering = ['title']
    
    # filter_backends = [SearchFilter]
    # search_fields = ['title', 'author', '=price']



    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'author', 'price']
