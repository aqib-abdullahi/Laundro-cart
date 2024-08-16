from django.contrib import admin
from .models import Category, Laundry, Order, GroupedOrder


admin.site.register(Category)
admin.site.register(Laundry)
admin.site.register(Order)
admin.site.register(GroupedOrder)