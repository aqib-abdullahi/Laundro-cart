from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def signup(request):
    """Sign Up page"""
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid entry')
    else:
        form = forms.SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

@ensure_csrf_cookie
def view_login(request):
    """Log in page"""
    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                Token.objects.filter(user=user).delete()
                token = Token.objects.create(user=user)
                login(request, user)
                if not user.is_superuser:
                    response = redirect('pickup')
                    response.set_cookie('authToken', token.key)
                    return response
                return HttpResponse("successfully logged in!")
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
@ensure_csrf_cookie
def logout_view(request):
    logout(request)
    return redirect('login')