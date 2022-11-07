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
            'nombre': forms.TextInput(attrs={'class':'form-control w-25'}),
            'cedula': forms.TextInput(attrs={'class':'form-control w-25'}),
            'idRol': forms.Select(attrs={'class':'form-control w-25'})
        }

class RegistrarMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        
        fields = [
            'identificador',
            'titulo',
            'cantidadRegistrada',
            'cantidadActual'
        ]
        labels = {
            'identificador': 'Identificador',
            'titulo': 'Titulo',
            'cantidadRegistrada': 'Cantidad a registrar',
            'cantidadActual' : ''
        }
        widgets = {
            'identificador': forms.TextInput(attrs={'class':'form-control w-25'}),
            'titulo': forms.TextInput(attrs={'class':'form-control w-25'}),
            'cantidadRegistrada': forms.NumberInput(attrs={'class':'form-control w-25', 'oninput':'actualizarValor()'}),
            'cantidadActual': forms.NumberInput(attrs={'class':'form-control w-25', 'style':'display:none'})
        }