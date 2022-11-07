from django.shortcuts import render, redirect
from django.http import HttpResponse
from .formularios import *
from .models import *

# Create your views here.
def home(request):
    title = 'Home'
    return render(request, "index.html", {'Titulo':title})

def prestamo(request):
    title = 'Prestamo'
    return render(request, "prestamo.html", {'Titulo':title})

def devolucion(request):
    title = 'Devolución'
    return render(request, "devolucion.html", {'Titulo':title})

def registrarPersona(request):
    title = 'Registrar Persona'
    if request.method == 'POST':
        form = RegistrarPersonaForm(request.POST)
        if form.is_valid():
            form.save()
            succes = 1
            return render(request, "registrarPersona.html", {'Titulo':title, 'form':form, 'succes': succes})
        else:
            succes = 2
            return render(request, "registrarPersona.html", {'Titulo':title, 'form':form, 'succes': succes})
    else:
        form = RegistrarPersonaForm()    
    return render(request, "registrarPersona.html", {'Titulo':title, 'form':form})

def eliminarPersona(request):
    title = 'Eliminar Persona'
    return render(request, "eliminarPersona.html", {'Titulo':title})

def registrarMaterial(request):
    title = 'Registrar Material'
    return render(request, "registrarMaterial.html", {'Titulo':title})

def aumentarMaterial(request):
    title = 'Aumentar Material'
    return render(request, "aumentarMaterial.html", {'Titulo':title})

def historial(request):
    title = 'Historial'
    return render(request, "historial.html", {'Titulo':title})
    