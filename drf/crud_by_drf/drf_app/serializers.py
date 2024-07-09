from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=50)
    address = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=20)
    phone_no = serializers.IntegerField()

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


