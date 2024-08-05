from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import Contactus, Cart, Orders, Product, CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .form import RegisterForm, CustomChangePasswordForm
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage


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
        cart = Cart.objects.filter(user=user, product=product)
        if not cart.exists():
            Cart.objects.create(user=user,product=product,total_price=price)
            messages.success(request, "{} added to your cart...".format(product.name))
        else:
            cart = cart.first()
            cart.quantity += 1
            cart.total_price = int(price) * cart.quantity
            cart.save()
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


class OrderView(View):

    @method_decorator(login_required)
    def get(self, request):
        return redirect('profile')
    
    @method_decorator(login_required)
    def post(self, request):
        carts = Cart.objects.filter(user=request.user)
        for cart in carts:
            Orders.objects.create(user=cart.user,product=cart.product,quantity=cart.quantity,total=cart.total_price)
            cart.delete()

        messages.success(request, 'Your order has been placed successfully')
        return redirect('home')


class CartView(View):
    @method_decorator(login_required)
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        total = cart.aggregate(total=Sum('total_price'))
        return render(request, 'cart.html', {'cart': cart, 'total_price':total})

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST.get('id')
        cart = Cart.objects.get(id=id)
        messages.success(request, "{} removed From your cart...".format(cart.product.name))
        cart.delete()
        return redirect('cart')



# Authentication
class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.GET.get('next')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in...")
            return redirect(next_url or 'home')
        messages.error(request, "Wrong User Name or Password")
        return redirect('login')


class UserRegister(View):
    def get(self, request):
        return render(request, 'register.html', {'form': RegisterForm()})
    
    def post(self, request):
        form_data = request.POST.dict() 
        image = request.FILES.get('image')

        if image:
            form_data['image'] = image 
        form = RegisterForm(form_data, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            if image:
                fs = FileSystemStorage()
                filename = fs.save("user_image/"+image.name, image)
                user.image = fs.url(filename)
            user.save()
            messages.success(request, "Successfully Registered...")
            return redirect('login')
        
        return render(request, 'register.html', {'form': form})


class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully Logged out...")
        return redirect('home')


class UserProfile(View):
    @method_decorator(login_required)
    def get(self, request):
        user_orders = Orders.objects.filter(user=request.user)
        return render(request, 'profile.html' ,{'orders': user_orders})


    @method_decorator(login_required)
    def post(self, request):
        username = request.user
        user = CustomUser.objects.get(username=username)
        image = request.FILES.get('image')
        print(image)
        if image:
            fs = FileSystemStorage()
            filename = fs.save("user_image/"+image.name, image)
            user.image = fs.url(filename)
            user.save()
            messages.success(request, "Successfully Updated Profile...")
            return redirect('profile')
        else:
            messages.error(request, "Please Upload Image...")
            return redirect('profile')
    

class UserChangePassword(View):
    template_name = 'change_password.html'
    form = CustomChangePasswordForm

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully...")
            return redirect('profile')
        messages.error(request, "Password not Changed...")
        return render(request, self.template_name, {'form': form})
