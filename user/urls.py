from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('pickup/', views.pickup, name="pickup"),
    path('profile/', views.profile, name="profile"),
    path('notifications/', views.notifications, name="notifications"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)