from django.shortcuts import render, HttpResponse
from .models import Student

def students(request):
    stu = Student.objects.all()
    return HttpResponse(stu)
