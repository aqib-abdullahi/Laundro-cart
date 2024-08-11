from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from core.models import Laundry, Order
from django.db.models import Sum


@login_required
def user_dashboard(request):
    return render(request, "user_dashboard.html")

@login_required
def pickup(request):
    laundry_items = Laundry.get_all_laundry()
    return render(request, 'pickup.html', {'laundry_items': laundry_items})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def notifications(request):
    return render(request, 'notifications.html')

@login_required
def orders(request):
    user = request.user
    user_orders = (Order.objects
                   .filter(user=request.user)
                   .values('order_group')
                   .annotate(total_quantity=Sum('quantity'), total_cost=Sum('cost'))
                   .order_by('-date'))
    context = {
        'user_orders': user_orders
    }
    return render(request, 'orders.html', context=context)
