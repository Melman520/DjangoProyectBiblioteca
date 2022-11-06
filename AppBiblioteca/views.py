from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def prestamo(request):
    return render(request, "prestamo.html")

def devolucion(request):
    return render(request, "devolucion.html")

def registrarPersona(request):
    return render(request, "registrarPersona.html")

def eliminarPersona(request):
    return render(request, "eliminarPersona.html")

def registrarMaterial(request):
    return render(request, "registrarMaterial.html")

def aumentarMaterial(request):
    return render(request, "aumentarMaterial.html")

def historial(request):
    return render(request, "historial.html")
    