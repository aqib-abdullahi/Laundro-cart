from django.shortcuts import render


def user_dashboard(request):
    return render(request, "user_dashboard.html")