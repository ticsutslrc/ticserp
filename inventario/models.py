# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(null=False, max_length=30)
    descripccion = models.CharField(null=True, blank=True, max_length=60)
    numero_inventario = models.CharField(null=False, max_length=10)
    codigo_barras = models.CharField(max_length=20, default='', blank=True)
    peso = models.PositiveIntegerField()

    ultimo_costo = models.DecimalField(max_digits=10, decimal_places=4)
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=4)

    cantidad_total_almacen = models.IntegerField(default=0)
    cantidad_minimo_almacen = models.PositiveIntegerField(default=5)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

