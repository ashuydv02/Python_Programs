from django.shortcuts import render
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee

class Employee_api(APIView):
    def get(self, request, id=None):
        id=request.data.get('id')
        if id is None:
                employee = Employee.objects.all()
                serializer_obj = EmployeeSerializer(employee, many=True)
                return Response(serializer_obj.data)
        else:
             try:
                employee = Employee.objects.get(id=id)
                serializer_obj = EmployeeSerializer(employee)
                return Response(serializer_obj.data)
             except:
                  return Response(
                       {'msg':'No Data Found'},
                       status=status.HTTP_404_NOT_FOUND,
                  )
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        try:
            id = request.data.get('id')
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()   
                return Response({'msg': 'Data Updated...'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg': 'Data does not exists...'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        try:
            id = request.data.get('id')
            employee = Employee.objects.get(id=id)
            if employee:
                employee.delete()
                return Response({'msg': 'Data Deleted...'}, status=status.HTTP_200_OK)
            return Response({"msg": "Data does not exists..."}, status=status.HTTP_200_OK)
        except:
            return Response({"msg": "Data does not exists..."}, status=status.HTTP_400_BAD_REQUEST)
