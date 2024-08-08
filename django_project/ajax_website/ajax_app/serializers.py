from rest_framework import serializers
from .models import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(write_only=True)
    verification_code = serializers.CharField(write_only=True, required=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'otp', 'phone_number', 'address', 'password1', 'password2', 'image', 'verification_code')

    def validate(self, data):
        if data['otp'] != data['verification_code']:
            raise serializers.ValidationError({'message': "Please Enter Correct Verification code."})
        
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'message': "Passwords do not match."})
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password1'])
        if 'image' in validated_data:
            user.image = validated_data['image']
        user.save()
        return user



class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Contactus.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['email'] == 'ay545153@gmail.com':
            raise serializers.ValidationError('Admin email is not allowed')
        return attrs
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance
