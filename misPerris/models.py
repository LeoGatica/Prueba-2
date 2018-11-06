from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length=100)
    rut = models.IntegerField()
    nombreCompleto= models.CharField(max_length=200)
    f_nacimiento = models.DateField()
    fono = models.IntegerField()
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30)
    tipoVivienda = models.CharField(max_length=30)


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
	
	


