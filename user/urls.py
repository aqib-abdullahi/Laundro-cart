from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('pickup/', views.pickup, name="pickup"),
    path('profile/', views.profile, name="profile"),
    path('notifications/', views.notifications, name="notifications"),
]