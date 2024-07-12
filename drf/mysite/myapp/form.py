from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class Register_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', 'address']