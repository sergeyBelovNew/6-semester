from .models import Equipment
from django.forms import ModelForm, TextInput, Textarea


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['id', 'title', 'type', 'description', 'cost']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название"
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Тип"
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание"
            }),
            "cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Стоимость"
            }),

        }