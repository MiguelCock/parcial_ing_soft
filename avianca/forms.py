from django import forms
from .models import Vuelo

class FormVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombre', 'tipo', 'precio']
        widgets = {
            'tipo': forms.Select(choices=Vuelo.TIPOS_VUELO),
        }