from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=250,
                                 label='',
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':"First name", 'class':'input'})
                                )
    last_name = forms.CharField(max_length=250,
                                label='',
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder':"Last name", 'class':'input'})
                               )
    email = forms.EmailField(max_length=250,
                             label='',
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder':"Email", 'class':'input'})
                            )
    password1 = forms.CharField(strip=False,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder':"Create Password", 'class':'input', 'id':'Password1'})
                               )
    password2 = forms.CharField(strip=False,
                                label='',
                                widget = forms.PasswordInput(attrs={'placeholder': "Confirm Password", 'class': 'input', 'id':'Password2'})
                               )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=250,
                                label='',
                                required=True,
                                widget=forms.EmailInput(attrs={'placeholder': "Email", 'class': 'input'})
                                )
    password = forms.CharField(strip=False,
                                label='',
                                widget=forms.PasswordInput(
                                attrs={'placeholder': "Password", 'class': 'input', 'id': 'Password'})
                                )