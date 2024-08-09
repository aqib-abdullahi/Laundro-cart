from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            print("valid form")
            try:
                user = form.save()
                return redirect('login')
            except Exception as e:
                print(f"error: {e}")
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
                login(request, user)
                if not user.is_superuser:
                    return redirect('dashboard')
                return HttpResponse("successfully logged ib!")
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request.user)
    return redirect('login')