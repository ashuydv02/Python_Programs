from django.shortcuts import render
from rest_framework.response import Response
from django.views import generic
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *

class HomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:8]
        return context

class MenuView(generic.TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CartViewApi(APIView):
    def post(self, request):
        id = request.data.get('id')
        if not id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity += 1
        cart.save()
        
        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)

class AboutView(generic.TemplateView):
    template_name = "about.html"

class ContactView(generic.TemplateView):
    template_name = "contact.html"

class ContactViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)



# ************************Authentication************************************************

class LoginView(generic.TemplateView):
    template_name = "login.html"

class LoginViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('name')
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
