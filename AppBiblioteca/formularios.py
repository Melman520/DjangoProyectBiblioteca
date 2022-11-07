from django import forms
from .models import *

class RegistrarPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'cedula',
            'idRol'
        ]
        labels = {
            'nombre': 'Nombre',
            'cedula': 'Cedula',
            'idRol': 'Rol'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'from-control'}),
            'cedula': forms.NumberInput(attrs={'class':'form-control w-25'}),
            'idRol': forms.Select(attrs={'class':'from-control'})
        }