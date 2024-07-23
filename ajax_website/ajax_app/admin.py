from django.contrib import admin
from .models import Contactus, CustomUser, Orders, Product, Cart, Category
from django.contrib.auth.admin import UserAdmin


class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price',)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    list_display = ('id', 'user', 'product', 'quantity', 'total', 'status', 'payment', 'created_at')
    

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Contactus)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Product)
admin.site.register(Cart, CartAdmin)
admin.site.register(Category)
