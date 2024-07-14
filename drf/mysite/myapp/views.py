from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import Contactus, Cart, Orders, Product, Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .form import Register_form

class Index(TemplateView):
    template_name = 'index.html'
    
class Menu(View):
    def get(self, requset):
        products = Product.objects.all()
        return render(requset, 'menu.html', {'products': products})

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST.get('product_id')
        product=Product.objects.get(id=id)
        price = request.POST.get('product_price')
        user = request.user
        Cart.objects.create(user=user,product=product,total_price=price)
        messages.success(request, "{} added to your cart...".format(product.name))
        return redirect('menu')

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

class Order_view(View):
    def get(self, request):
        return render(request, 'order.html')
    
class Cart_view(View):
    @method_decorator(login_required)
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        return render(request, 'cart.html', {'cart': cart})

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST.get('id')
        cart = Cart.objects.get(id=id)
        messages.success(request, "{} removed From your cart...".format(cart.product.name))
        cart.delete()
        return redirect('cart')



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

class User_profile(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'profile.html')

