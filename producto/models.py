from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    nombre = models.CharField(max_length=40, blank=True)
    imagen = models.ImageField(upload_to="tienda", blank=True, null=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=240, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nombre
