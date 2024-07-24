from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from django.views import generic
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage


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
    
    def delete(self, request, id):
        if not id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            cart = Cart.objects.get(id=id)
            cart.delete()
            return Response({'message': 'Item is removed...'}, status=status.HTTP_200_OK)
        
        except Cart.DoesNotExist:
            return Response({'message': 'Cart item is not found'}, status=status.HTTP_200_OK)

    def update(self, request, id):
        quantity = request.data.get('quantity')
        if not id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not quantity:
            return Response({'error': 'Quantity is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            cart = Cart.objects.get(id=id)
            cart.quantity = quantity
            cart.save()
            return Response({'message': 'Product quantity updated'}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    

class OrderViewApi(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        carts = Cart.objects.filter(user=user)
        if not carts.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        for cart in carts:
            Orders.objects.create(
                user=user, 
                product=cart.product, 
                quantity=cart.quantity, 
                total=cart.total_price
            )
            cart.delete()
        messages.success(request, "Your Order has been succesfully palced...")
        return Response({'message': 'Order placed successfully'}, status=status.HTTP_200_OK)

class CartView(generic.View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        total = cart.aggregate(total=Sum('total_price'))
        return render(request, 'cart.html', {'cart': cart, 'total_price':total})


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
            messages.success(request, "Successfully logged in...")
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out...")
        return redirect('login')


class RegisterView(generic.TemplateView):
    template_name = 'register.html'


class RegisterViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Successfully Registered...")
            return Response({'message': "Successfully Registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generic.View):
    template_name = 'profile.html'

    def get(self, request):
        orders = Orders.objects.filter(user=request.user)
        return render(request, self.template_name, {'orders': orders})

    def post(self, request):
        username = request.user
        user = CustomUser.objects.get(username=username)
        image = request.FILES.get('image')
        print(image)
        if image:
            fs = FileSystemStorage()
            filename = fs.save("user_image/"+image.name, image)
            user.image = fs.url(filename)
            user.save()
            messages.success(request, "Successfully Updated Profile...")
            return redirect('profile')
        else:
            messages.error(request, "Please Upload Image...")
            return redirect('profile')