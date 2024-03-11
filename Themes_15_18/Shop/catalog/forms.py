from django import forms
from .models import *


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['manufacturer', 'name', 'description', 'quantity', 'price', 'category']