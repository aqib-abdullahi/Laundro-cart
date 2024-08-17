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
    
    def save(self, commit=True):
        """saves user profile update"""
        user = super(ProfileUpdateForm, self).save(commit=False)
        if user.first_name and user.last_name and user.phone_number and user.address:
            user.profile_completed = True
        if commit:
            user.save()
        return user