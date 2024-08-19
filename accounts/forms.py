from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, BaseUserManager, AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser


User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=250,
                                 label='First name:',
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':"First name",
                                                               'class':'input', 'id': 'firstname'})
                                )
    last_name = forms.CharField(max_length=250,
                                label='Last name:',
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder':"Last name",
                                                              'class':'input', 'id': 'lastname'})
                               )
    email = forms.EmailField(max_length=250,
                             label='Email:',
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder':"Email",
                                                            'class':'input', 'name':'email', 'id':'email'})
                            )
    password1 = forms.CharField(strip=False,
                                label='Password:',
                                widget=forms.PasswordInput(attrs={'placeholder':"Create Password",
                                                                  'class':'input', 'id':'password1',
                                                                  'autocomplete': 'new-password'})
                               )
    password2 = forms.CharField(strip=False,
                                label='Confirm Password:',
                                widget = forms.PasswordInput(attrs={'placeholder': "Confirm Password",
                                                                    'class': 'input', 'id':'password2',
                                                                    'autocomplete': 'new-password'})
                               )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password2'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=250,
                                label='Email:',
                                required=True,
                                widget=forms.EmailInput(attrs={'placeholder': "Email", 'class': 'input', 'id': 'email'})
                                )
    password = forms.CharField(strip=False,
                                label='Password:',
                                widget=forms.PasswordInput(
                                attrs={'placeholder': "Password", 'class': 'input', 'id': 'password'})
                                )