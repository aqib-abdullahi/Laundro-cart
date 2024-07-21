from django.db import models
from django.forms import ModelForm
from accounts.models import CustomUser

class ProfileUpdateForm(ModelForm):
    """Form for user information update"""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']