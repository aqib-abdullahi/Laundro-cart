from rest_framework import serializers
from core.models import Order
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_group', 'laundry', 'quantity', 'cost', 'address', 'phone', 'date', 'status']

