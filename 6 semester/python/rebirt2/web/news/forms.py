from .models import Document
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['id', 'title', 'ad', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи"
            }),
            "ad": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс"
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст"
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата"
            }),
        }