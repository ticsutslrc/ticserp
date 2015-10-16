# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Venta(models.Model):
    total = models.DecimalField(decimal_places=4, max_digits=10)
    subtotal = models.DecimalField(decimal_places=4, max_digits=10)
    impuestos = models.DecimalField(decimal_places=4, max_digits=10)
    productos = models.ManyToManyField('inventario.Producto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class Cliente(models.Model):
    nombre = models.CharField(null=False, max_length=30)
    compania = models.CharField(null=True, blank=True, max_length=50)
    direccion = models.CharField(null=True, blank=True, max_length=100)
    ubicacion = models.CharField(null=True, blank=True, max_length=20)
    telefono = models.CharField(null=True, blank=True, max_length=15)
    correo = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nombre