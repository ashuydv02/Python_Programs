from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, Blocklist
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import permissions

from django.core.cache import cache
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Example of Caching
class CachedDataView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'Book_data'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            data = list(Book.objects.all().values())
            cache.set(cache_key, data, 60*10) 
        else:
            data = cached_data

        return Response(data)


# Example of Custom Permissions
class BlocklistPermission(permissions.BasePermission):
    message = "This ip is block..."

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip=ip_addr).exists()
        return not blocked


class BookView(APIView):
    permission_classes = [BlocklistPermission]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Example of throttling
class AuthorView(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
