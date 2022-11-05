from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        documento = request.POST['documento']
        try:
            Persona.objects.get(cedula=documento)
            return render(request, "RegistrarMaterial.html")
        except:
            return HttpResponse('Usuario no encontrado')