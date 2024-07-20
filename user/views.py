from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileUpdateForm


@login_required
def user_dashboard(request):
    return render(request, "user_dashboard.html")

@login_required
def pickup(request):
    return render(request, 'pickup.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile.html', {'form': form})

@login_required
def notifications(request):
    return render(request, 'notifications.html')