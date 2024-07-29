from django.urls import path
from . import views

urlpatterns = [
    path('v1/request-pickup', views.create_pickup_order, name='request_pickup'),
    path('v1/token/login', views.user_login_token, name='user_login_token'),
    path('v1/logout', views.user_logout_token, name='user_logout_token')
]