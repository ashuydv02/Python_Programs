from rest_framework import serializers
from .models import CustomUser, Cart, Category, Contactus, Product, Orders


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'image', 'address']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
            }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True}
            }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'write_only': True}
            }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'write_only': True}
            }


class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'write_only': True}
            }
