from django.db import models

# Create your models here.

class Familiar(models.Model):
    cedula_identidad = models.IntegerField()
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()