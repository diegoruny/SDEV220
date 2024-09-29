from django.db import models
from django import forms

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'user_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Use a password input for the password field
        }

