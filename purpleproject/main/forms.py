from django import forms
from .models import Foto
from django.forms import ClearableFileInput

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('img',)

        widgets = {
            "img":ClearableFileInput(attrs={
                'class': 'file-input'
            })
        }