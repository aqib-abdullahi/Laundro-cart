from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import forms
from django.contrib import messages


def signup(request):
    """Sign Up page"""
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Invalid entry')
    else:
        form = forms.SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def view_login(request):
    """Log in page"""
    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("successfully logged ib!")
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})