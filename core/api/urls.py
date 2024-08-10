from django.urls import path
from . import views

urlpatterns = [
    path('v1/request-pickup', views.create_pickup_order, name='request_pickup'),
]