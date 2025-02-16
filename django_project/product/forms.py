from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'expiration_date', 'appearance', 'proteins', 'fats', 'carbohydrates']
