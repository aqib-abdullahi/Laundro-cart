import datetime

from django.db import models
from django.conf import settings


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
        return Laundry.objects.filter(id__in=id)

    @staticmethod
    def get_all_laundry():
        """Returns all laundry"""
        return Laundry.objects.all()

    @staticmethod
    def get_all_laundry_by_categoryid(category_id):
        """returns all laundry based on a category id"""
        if category_id:
            return Laundry.objects.filter(category=category_id)
        else:
            return Laundry.get_all_laundry()

class Order(models.Model):
    """Orders"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled','Cancelled'),
    ])

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

    @staticmethod
    def get_orders_by_user(user):
        """returns orders by a customer based on user"""
        return Order.Objects.filter(user=user).order_by('-date')