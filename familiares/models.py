from django.db import models

# Create your models here.

class Familiares(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
