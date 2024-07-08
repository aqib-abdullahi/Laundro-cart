from django.shortcuts import render


def signup(request):
    """Sign Up page"""
    return render(request, 'signup.html')

def login(request):
    """Log in page"""
    return render(request, 'login.html')