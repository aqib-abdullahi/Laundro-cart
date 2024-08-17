from django.shortcuts import redirect
from django.urls import reverse

def profile_completion_required(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if not user.first_name or not user.last_name or not user.address or not user.phone_number:
                return redirect(reverse('profile'))
        return view_func(request, *args, **kwargs)
    return wrapper