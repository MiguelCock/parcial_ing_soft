from django import forms
from .models import Vuelo

class FlightVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombre', 'tipo_de_vuelo', 'precio']
        widgets = {
            'tipo_de_vuelo': forms.Select(choices=Vuelo.TIPOS_VUELO),
        }