from django.forms import ModelForm
from .models import Laundry, Order


class OrderForm(ModelForm):
    """Order form"""
    class Meta:
        model = Order
        fields = ['laundry', 'quantity', 'cost', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user