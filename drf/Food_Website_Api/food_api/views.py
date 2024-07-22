from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartView(APIView):
    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        if cart is None:
            return Response({'message': 'Cart not found'})
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        product = Product.objects.get(id=request.data['id'])
        cart = Cart.objects.get(user=request.user)
        if cart is None:
            cart = Cart.objects.create(user=request.user)
            cart.products.add(product)
            cart.save()
            return Response({'message': 'Product added to cart'})
        return Response({'message': 'Product added to cart'})


class OrderView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class OrderViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class UserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ContactusView(generics.ListCreateAPIView):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer
