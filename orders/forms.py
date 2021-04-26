from django import forms
from django.forms import ModelForm, DateInput
from .models import Orders

from django.contrib.auth.models import User


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        exclude=['price','price_with_cod','price_with_return_charges']
        widgets = {
            'weight': forms.TextInput(attrs={'placeholder':'Weights in KG'}),
            'location': forms.TextInput(attrs={'placeholder':'Your Delivery Location/Full Address'}),
        }
        