from django import forms
from django.forms import ModelForm

EQUIPMENT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddEquipmentForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=EQUIPMENT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
