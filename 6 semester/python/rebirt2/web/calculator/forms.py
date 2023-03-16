from django.forms import ModelForm, TextInput, Textarea


class EquipmentForm(ModelForm):
    class Meta:
        model = Equepment
        fields = ['id', 'title', 'type', 'description', 'cost']

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

        }