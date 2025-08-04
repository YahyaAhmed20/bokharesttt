from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone', 'landmark', 'delivery_method']
        widgets = {
            'delivery_method': forms.RadioSelect
        }
