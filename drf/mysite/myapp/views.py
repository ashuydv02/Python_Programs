from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Contactus
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import Register_form

class Index(TemplateView):
    template_name = 'index.html'
    
class Menu(TemplateView):
    template_name = 'menu.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contactus.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')

class Order(View):
    def get(self, request):
        return render(request, 'order.html')






# Authentication
class User_login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in...")
            return redirect(next_url or 'home')
        messages.error(request, "Wrong User Name or Password")
        return redirect('login')

class User_register(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered...")
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class User_logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully Logged out...")
        return redirect('home')

