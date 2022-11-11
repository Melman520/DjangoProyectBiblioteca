from django.shortcuts import render, redirect
from .formularios import *
from .models import *

# Create your views here.

def home(request):
    title = 'Home'
    return render(request, "index.html", {'Titulo':title})

def usuarios(request, eliminacion):
    title = 'Usuarios'
    personas = Persona.objects.all()
    return render(request, "usuarios.html", {'Titulo':title, 'personas':personas, 'eliminacion': eliminacion})

def materiales(request):
    title = 'Materiales'
    materiales = Material.objects.all()
    return render(request, "materiales.html", {'Titulo':title, 'materiales': materiales})

def materialesPrestamo(request, documento):
    title = 'Materiales'
    materiales = Material.objects.all()
    persona = Persona.objects.get(cedula=documento)
    rol = str(persona.idRol)
    materialesPrestados = MaterialPrestado.objects.filter(cedula=documento)
    return render(request, "materialesPrestamo.html", {'Titulo':title, 'materiales': materiales, 'persona':persona, 'materialesPrestados':materialesPrestados, 'rol': rol})

def hacerPrestamo(request, documento, idmaterial):
    persona = Persona.objects.get(cedula=documento)
    material = Material.objects.get(identificador=idmaterial)
    material.cantidadActual = material.cantidadActual - 1
    material.save()
    MaterialPrestado.objects.create(cedula=persona, idMaterial=material)
    generarRegistro(persona, material, 'Prestamo')
    return redirect('MaterialesPrestamo', documento)

def materialesDevolver(request, documento):
    title = 'Devolver Materiales'
    materiales = MaterialPrestado.objects.filter(cedula=documento)
    persona = Persona.objects.get(cedula=documento)
    return render(request, "materialesDevolver.html", {'Titulo':title, 'materiales': materiales, 'persona':persona})

def hacerDevolucion(request, documento, idmaterial):
    persona = Persona.objects.get(cedula=documento)
    material = Material.objects.get(identificador=idmaterial)
    material.cantidadActual = material.cantidadActual + 1
    material.save()
    materialRegistro = MaterialPrestado.objects.filter(cedula=documento).first()
    materialRegistro.delete()
    generarRegistro(persona, material, 'Devolución')
    return redirect('MaterialesDevolver' ,documento )

def registrarPersona(request):
    title = 'Registrar Persona'
    if request.method == 'POST':
        form = RegistrarPersonaForm(request.POST)
        if form.is_valid():
            form.save()
            succes = 1
            eliminado=1
            return redirect("usuarios" , eliminado)
        else:
            succes = 2
            return render(request, "registrarPersona.html", {'Titulo':title, 'form':form, 'succes': succes})
    else:
        form = RegistrarPersonaForm()    
        return render(request, "registrarPersona.html", {'Titulo':title, 'form':form})

def eliminarPersona(request, documento):
    materialesPrestados = MaterialPrestado.objects.filter(cedula=documento)
    persona = Persona.objects.get(cedula=documento)
    if(len(materialesPrestados) == 0):
        persona.delete()
        eliminado = 2
        return redirect("usuarios" , eliminado)
    else:
        eliminado = 3
        return redirect("usuarios", eliminado)

def registrarMaterial(request):
    title = 'Registrar Material'
    if request.method == 'POST':
        form = RegistrarMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Materiales')
        else:
            succes = 2
            return render(request, "registrarMaterial.html", {'Titulo':title, 'form':form, 'succes': succes})
    else:
        form = RegistrarMaterialForm()
        return render(request, "registrarMaterial.html", {'Titulo':title, 'form':form})


def edicionMaterial(request, identificador):
    title = 'Aumentar Material'
    material = Material.objects.get(identificador=identificador)
    if request.method == 'POST':
        form = AumentarMaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect("Materiales")
    else:
        form = AumentarMaterialForm()
        return render(request, "edicionMaterial.html", {'Titulo':title, 'material': material, 'form':form})

def historial(request):
    title = 'Historial'
    registros = reversed(Registro.objects.all())
    return render(request, "historial.html", {'Titulo':title, 'registros': registros})

def generarRegistro(documento, idmaterial, estado):
    Registro.objects.create(idMaterial=idmaterial, movimiento=estado, cedula=documento)