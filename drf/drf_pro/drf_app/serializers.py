from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
# Model Serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


# Serializer

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(
        max_length=50,
        validators=[UniqueValidator(queryset=Employee.objects.all(), message="Unique mail dalo bhai")]
    )
    address = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=20)
    phone_no = serializers.IntegerField(
        validators=[MinValueValidator(6000000000), MaxValueValidator(9999999999)]
    )

    # def validate(self, data):
    #     if 10 < len(str(data['phone_no'])) or len(str(data['phone_no'])) < 10:
    #         raise serializers.ValidationError("The phone Number Should be of 10 digits.")
        
    #     employee = Employee.objects.filter(email=data['email'])
    #     if employee:
    #         raise serializers.ValidationError("Email already exists...")
    #     return data


    def create(self, data):
        new_data = Employee.objects.create(**data)
        return new_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.department = validated_data.get("department", instance.department)
        instance.address = validated_data.get("address", instance.address)
        instance.phone_no = validated_data.get("phone_no", instance.phone_no)
        instance.save()
        return instance


