import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings
import uuid
import random


class Category(models.Model):
    """Category models"""
    name = models.CharField(max_length=50)

    @staticmethod
    def get_categories():
        """returns all categories"""
        return Category.objects.all()

    def __str__(self):
        return self.name

class Laundry(models.Model):
    """Clothings, sheets e.t.c"""
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True
    )
    image = models.ImageField(upload_to='uploads/products')

    @staticmethod
    def get_laundry_by_id(id):
        """Returns a laundry based on id"""
        return Laundry.objects.get(id__in=id)

    @staticmethod
    def get_all_laundry():
        """Returns all laundry"""
        return Laundry.objects.all()

    @staticmethod
    def get_all_laundry_by_category_name(category_name):
        """returns all laundry based on a category id"""
        if category_name:
            return Laundry.objects.filter(category=category_name)
        else:
            return Laundry.get_all_laundry()

class Order(models.Model):
    """Orders"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_group = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled','Cancelled'),
    ])
    order_no = models.CharField(max_length=6, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = str(random.randint(100000, 999999))
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_no} by {self.user.email}"

    @staticmethod
    def get_orders_by_user_id(user_id):
        """returns orders by a customer based on user"""
        return Order.objects.filter(user_id=user_id)
    
    @staticmethod
    def get_orders_by_group_id(request, order_group_id):
        """returns orders based on given order group id
        (order requests made at once)
        """
        return Order.objects.filter(order_group=order_group_id, user=request.user)
