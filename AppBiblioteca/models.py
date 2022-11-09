from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key = True, null= False)
    rol = models.CharField(max_length = 50, null= False)
    def __str__(self):
        return '{}'.format(self.rol)

class Persona(models.Model):
    nombre = models.CharField(max_length = 50, null= False)
    cedula= models.IntegerField(primary_key = True, null = False)
    idRol = models.ForeignKey(Rol, on_delete = models.CASCADE)
    def __str__(self):
        return '{}'.format(self.cedula)

class Material(models.Model):
    identificador = models.IntegerField(primary_key = True, null = False)
    titulo = models.CharField(max_length = 50, null= False)
    fechaRegistro = models.DateField(auto_now_add = True)
    cantidadRegistrada = models.PositiveIntegerField(null = False)
    cantidadActual = models.PositiveIntegerField(null = False)
    def __str__(self):
        return '{}'.format(self.identificador)

class Registro(models.Model):
    id = models.AutoField(primary_key = True, null= False)
    idMaterial= models.ForeignKey(Material, on_delete = models.CASCADE)
    movimiento = models.CharField(max_length = 50, null = False)
    cedula = models.ForeignKey(Persona, on_delete = models.CASCADE)
    fecha = models.DateField(auto_now_add = True)

class MaterialPrestado(models.Model):
    id = models.AutoField(primary_key = True, null= False)
    cedula = models.ForeignKey(Persona, on_delete = models.CASCADE)
    idMaterial = models.ForeignKey(Material, on_delete = models.CASCADE)