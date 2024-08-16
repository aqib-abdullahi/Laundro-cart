from typing import Any, Mapping
from django.core.files.base import File
from django.db import models
from django.forms import ModelForm
from django.forms.utils import ErrorList
from accounts.models import CustomUser

class ProfileUpdateForm(ModelForm):
    """Form for user information update"""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True