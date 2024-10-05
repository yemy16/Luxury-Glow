from django.forms import ModelForm
from .models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "shade_name", "stock_quantity"]
