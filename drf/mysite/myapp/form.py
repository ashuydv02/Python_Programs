from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', 'address']

class CustomChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'old_password', 'new_password1', 'new_password2']
