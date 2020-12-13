from django.db import models

# Create your models here.
class Newsletter(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=30)
    imagen = models.CharField(max_length=30)
    target = models.CharField(max_length=30)
    frecuencia = models.CharField(max_length=30)
    fecha =  models.DateField()
