from rest_framework import serializers
from core.models import Order
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class SignUpSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email already exists")
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user