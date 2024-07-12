from django.contrib import admin
from .models import Contactus, CustomUser, Orders, Product, Cart
from django.contrib.auth.admin import UserAdmin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date')


admin.site.register(Contactus, ContactAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Cart)