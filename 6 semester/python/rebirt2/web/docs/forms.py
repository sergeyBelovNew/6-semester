from django import forms
from django.forms import Form


class UploadFileForm(Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()