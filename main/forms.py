from django.forms import ModelForm
from .models import SkincareMakeupEntry

class SkincareMakeupEntryForm(ModelForm):
    class Meta:
        model = SkincareMakeupEntry
        fields = ["name", "price", "description","shade_name","stock_quantity"]