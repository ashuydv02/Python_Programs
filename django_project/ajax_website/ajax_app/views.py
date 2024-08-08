from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from django.views import generic
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *
from django.db.models import Sum, F
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.conf import settings
import random
import stripe


class HomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:8]
        return context


class MenuView(generic.TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CartView(LoginRequiredMixin, generic.View):
    def get(self, request):
        cart = CartItem.objects.filter(cart__user=request.user)
        total = cart.aggregate(total=Sum(F('quantity') * F('product__price')))
        return render(request, 'cart.html', {'cart': cart, 'total_price':total})


class CartViewApi(APIView):
    def post(self, request):
        id = request.data.get('id')
        if not id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            cart_item.quantity += 1
        cart_item.save()
        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        if not id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            cart = CartItem.objects.get(id=id)
            cart.delete()

            cart = CartItem.objects.filter(cart__user=request.user)
            total = cart.aggregate(total=Sum(F('quantity') * F('product__price')))
            return Response({'message': 'Product removed from cart', 'total': total['total']},
                            status=status.HTTP_200_OK)
        
        except Cart.DoesNotExist:
            return Response({'message': 'Cart item is not found'}, status=status.HTTP_200_OK)


class UpdateCartViewApi(APIView):
    def put(self, request, id, format=None):
        try:
            cart_item = CartItem.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            updated_item = serializer.save()
            cart = CartItem.objects.filter(cart__user=request.user)
            total = cart.aggregate(total=Sum(F('quantity') * F('product__price')))
            response_data = {
                'quantity': updated_item.quantity,
                'total_price': total,
            }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderViewApi(LoginRequiredMixin, generic.View):
    def post(self, request):
        user = request.user
        data = request.POST
        request.session['payment_method'] = data['payment_method']
        if not user.is_authenticated:
            messages.success(request, "Please login first...")
            return redirect('cart')

        carts = CartItem.objects.filter(cart__user=user)
        if not carts.exists():
            messages.success(request, "No items in the cart...")
            return redirect('cart')

        if data['payment_method'] == 'c':
            try:
                checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items = [
                {
                    "price_data": {
                        "currency": "inr",
                        "unit_amount": int(item.product.price) * 100,
                        "product_data": {
                            "name": item.product.name,
                        },
                    },
                    "quantity": int(item.quantity),
                }
                for item in carts
                ],
                mode='payment',
                success_url= 'http://127.0.0.1:8000/success',
                cancel_url='http://127.0.0.1:8000/cancel',
                )
            except Exception as err:
                messages.error(request, str(err))
                return redirect('cart')

        try:
            return redirect(checkout_session.url, code=303)
        except:
            return redirect('success')


class PaySuccessView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        carts = CartItem.objects.filter(cart__user=request.user)
        order = Orders.objects.create(user=request.user, payment=request.session['payment_method'])
        for cart in carts:
            OrderItem.objects.create(
                order=order,
                product=cart.product, 
                quantity=cart.quantity,
            )

        carts.delete()
        messages.success(request, "Your Order has been succesfully placed and delivered to your registered address...")
        return redirect('home')


class PayCancelView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        messages.error(request, "Some Error Occured so please try again...")
        return redirect('cart')


class AboutView(generic.TemplateView):
    template_name = "about.html"


class ContactView(generic.TemplateView):
    template_name = "contact.html"


class ContactViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)


# ************************Authentication************************************************

class LoginView(generic.TemplateView):
    template_name = "login.html"


class LoginViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('name')
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in...")
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "Username or password is wrong..."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out...")
        return redirect('login')


class RegisterView(generic.TemplateView):
    template_name = 'register.html'


class RegisterViewApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data.copy()
        data['verification_code'] = request.session.get('verification_code')
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            del request.session['verification_code']
            messages.success(request, "Successfully Registered...")
            return Response({'message': "Successfully Registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(LoginRequiredMixin, generic.View):
    template_name = 'profile.html'

    def get(self, request):
        orders = OrderItem.objects.filter(order__user=request.user)
        return render(request, self.template_name, {'orders': orders})

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


class Send_Verification_Code(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        if CustomUser.objects.filter(email=email).exists():
                return Response({'message': "Email is already verified and exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            code = str(random.randint(100000, 999999))
            try:
                mail_content = "Your Verification Code is: "+code
                send_mail(
                    "Mail Verification Code",
                    mail_content,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                request.session['verification_code'] = code
                return Response({'message': "Verification Code Sent Successfully"}, status=status.HTTP_200_OK)
            except BadHeaderError:
                return Response({'message': "Something Went Wrong Please try Again."}, status=status.HTTP_400_BAD_REQUEST)
            except SMTPException as e:
                return Response({'message': "Something Went Wrong Please Try Again."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

