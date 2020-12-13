from django.db import models

# Create your models here.
class Tag(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.CharField(max_length=30)
    fecha =  models.DateField()
