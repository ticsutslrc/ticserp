# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Venta(models.Model):
    num_factura = models.SlugField(max_length=10)
    fecha = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey('ventas.Cliente', null=True)

    producto = models.ForeignKey('inventario.Producto', null=False)
    precio = models.DecimalField(decimal_places=4, max_digits=10)
    cantidad = models.IntegerField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    compras = models.BooleanField(default=False)
    produccion = models.BooleanField(default=False)
    planeacion = models.BooleanField(default=False)
    inventario = models.BooleanField(default=False)

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return str(self.pk)


class Cliente(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    rfc = models.CharField(null=False, max_length=50)
    direccion = models.CharField(null=False, max_length=100)
    ciudad = models.CharField(null=False, max_length=100)
    estado = models.CharField(null=False, max_length=30)
    pais = models.CharField(null=False, max_length=30)
    giro = models.CharField(null=False, max_length=50) 
    correo = models.CharField(null=False, max_length=60)
    telefono = models.CharField(null=False, max_length=20)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nombre


class ContactoCliente(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    puesto = models.CharField(null=False, max_length=40)
    telefono = models.CharField(null=False, max_length=20)
    correo = models.CharField(null=False, max_length=60)
    cliente = models.ForeignKey('ventas.Cliente', null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nombre