from django.db import models
from django.utils import timezone

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Anonimo")
    nacionalidad = models.CharField(max_length=100, default="Sin especificar")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_creacion = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100, default="Sin genero")
    fecha_publicacion = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
