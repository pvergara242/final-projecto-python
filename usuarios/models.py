from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=30)
    Correo = models.EmailField()
    Contrasena = models.CharField(max_length=30)
    fecha =  models.DateField()