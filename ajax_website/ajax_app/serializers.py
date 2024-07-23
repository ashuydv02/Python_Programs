from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

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
