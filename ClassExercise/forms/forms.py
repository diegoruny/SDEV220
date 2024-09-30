from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
