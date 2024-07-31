from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import mixins, generics

from .models import Employee
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer, UserSerializer

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token

# @api_view(['GET'])
# def api_route(request, format=None):
#     return Response({
#         'user_api': reverse('user_api', request=request, format=format),
#         'crud_api': reverse('employee_api', request=request, format=format)
#     })



# Custom keyword for token
class CustomAuthentication(TokenAuthentication):
    keyword = 'Bearer'

class User_api(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]


# Using generic class-based views
class Employee_api(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [BasicAuthentication]

class Employee_api_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [BasicAuthentication]


# Custom Token Auth creation by username and password

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
    

# Using mixins
# class Employee_api(
#         mixins.ListModelMixin,
#         mixins.CreateModelMixin,
#         generics.GenericAPIView,
# ):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class Employee_api_details(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
    
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, * args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(self, request, *args, **kwargs)





# Function Base Api View
# @api_view(['GET', 'POST'])
# def employee_list(request, format=None):
#     if request.method == 'GET':
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request, pk, format=None):
#     try:
#         employee = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = request.data
#         serializer = EmployeeSerializer(employee, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         employee.delete()
#         return Response({'msg': 'Data Deleted...'}, status=status.HTTP_200_OK)





# Function Base view
# @csrf_exempt
# def employee_list(request):
#     if request.method == 'GET':
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def employee_detail(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(employee, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status=204)





# Class Base Api View
# class Employee_api(APIView):
#     def get(self, request, id=None):
#         id=request.data.get('id')
#         if id is None:
#                 employee = Employee.objects.all()
#                 serializer_obj = EmployeeSerializer(employee, many=True)
#                 return Response(serializer_obj.data)
#         else:
#              try:
#                 employee = Employee.objects.get(id=id)
#                 serializer_obj = EmployeeSerializer(employee)
#                 return Response(serializer_obj.data)
#              except:
#                   return Response(
#                        {'msg':'No Data Found'},
#                        status=status.HTTP_404_NOT_FOUND,
#                   )
#     def post(self, request, format=None):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, format=None):
#         try:
#             id = request.data.get('id')
#             employee = Employee.objects.get(id=id)
#             serializer = EmployeeSerializer(employee, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()   
#                 return Response({'msg': 'Data Updated...'}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({'msg': 'Data does not exists...'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request, format=None):
#         try:
#             id = request.data.get('id')
#             employee = Employee.objects.get(id=id)
#             if employee:
#                 employee.delete()
#                 return Response({'msg': 'Data Deleted...'}, status=status.HTTP_200_OK)
#             return Response({"msg": "Data does not exists..."}, status=status.HTTP_200_OK)
#         except:
#             return Response({"msg": "Data does not exists..."}, status=status.HTTP_400_BAD_REQUEST)
