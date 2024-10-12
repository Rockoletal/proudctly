from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nombe = models.CharField(max_length=255)

    def __str__(self):
        return self.nombe


class Producto(models.Model):

    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # Cascade: Eliminar el producto
    # Protect: Lanza un error
    # Restrict: Solo elimina si no existen productos
    # Set_null: Actualiza un valor nulo
    # Set_default: asigna valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre
