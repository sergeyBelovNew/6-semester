from .models import Equipment
from django.forms import ModelForm, TextInput, Textarea

EQUIPMENT_QUANTITY_CHOICES = [(i, str(i) for i in range(1, 21))]
class CartAddEquipmentFrom(ModelForm):
    quantity = forms.TypedChoiceField(choices = EQUIPMENT_QUANTITY_CHOICES, coerce = false)
    override = forms.TypedChoiceField(choices = EQUIPMENT_QUANTITY_CHOICES, coerce = false)