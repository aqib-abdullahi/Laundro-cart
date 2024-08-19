from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from core.models import Laundry, Order, GroupedOrder
from django.contrib import messages
from .decorators import profile_completion_required


@login_required
def user_dashboard(request):
    return render(request, "user_dashboard.html")

@profile_completion_required
@login_required
def pickup(request):
    laundry_items = Laundry.get_all_laundry()
    return render(request, 'pickup.html', {'laundry_items': laundry_items})


@login_required
def profile(request):
    def replace_message(request, level, new_message):
        storage = messages.get_messages(request)
        storage.used = False
        new_storage = []
        for message in storage:
            if message.level != level:
                new_storage.append(message)
        storage._queued_messages = new_storage
        messages.add_message(request, level, new_message)
        return
    
    user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            if not user.address or not user.phone_number:
                replace_message(request, messages.WARNING, 'Please complete your profile before requesting pickup!')
            return render(request, 'profile.html', {'form': form})
    else:
        form = ProfileUpdateForm(instance=request.user)    

    if request.method != 'POST' and (not user.address or not user.phone_number):
        replace_message(request, messages.WARNING, 'Please complete your profile before requesting pickup!')
    return render(request, 'profile.html', {'form': form})

@login_required
def notifications(request):
    return render(request, 'notifications.html')

@login_required
def orders(request):
    user = request.user
    user_orders = GroupedOrder.objects.filter(user=user).order_by('-date')
    context = {
        'user_orders': user_orders
    }
    return render(request, 'orders.html', context=context)