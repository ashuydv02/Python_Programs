from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('password',)

    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contactus)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
