from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length = 50, null= False)
    cedula= models.IntegerField(primary_key = True, null = False)
    rol = models.CharField(max_length = 50, null = False)

class Material(models.Model):
    identificador = models.IntegerField(primary_key = True, null = False)
    titulo = models.CharField(max_length = 50, null= False)
    fechaRegistro = models.DateField(auto_now_add = True)
    cantidadRegistrada = models.IntegerField(null = False)
    cantidadActual = models.IntegerField(null = False)

class Registro(models.Model):
    identificador= models.IntegerField(primary_key = True, null = False)
    prestado = models.BooleanField(null = False)
    cedula = models.ForeignKey(Persona, on_delete = models.CASCADE)
    fecha = models.DateField(auto_now_add = True)

class MaterialPrestado(models.Model):
    id = models.AutoField(primary_key = True, null= False)
    cedula = models.ForeignKey(Persona, on_delete = models.CASCADE)
    idMaterial = models.ForeignKey(Material, on_delete = models.CASCADE)