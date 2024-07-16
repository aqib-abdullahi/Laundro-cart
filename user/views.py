from django.shortcuts import render


def user_dashboard(request):
    return render(request, "user_dashboard.html")

def pickup(request):
    return render(request, 'pickup.html')

def profile(request):
    return render(request, 'profile.html')

def notifications(request):
    return render(request, 'notifications.html')