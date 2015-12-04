# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Proveedor(models.Model):
	num_proveedor = models.IntegerField(default=0)
	nombre = models.CharField(null=False, max_length=100)
	RFC = models.CharField(null=True, blank=True, max_length=15)
	giro = models.CharField(null=True, max_length=100)
	direccion = models.CharField(null=False, max_length=50)
	ciudad = models.CharField(null= False, max_length=30)
	estado = models.CharField(null= False, max_length=30)
	pais = models.CharField(null= False, max_length=30)
	telefono = models.CharField(null= False, max_length=20)
	correo = models.CharField(null= False, max_length=20)
	comentario = models.CharField(null=True, max_length=100)
	
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __str__(self):
		return self.nombre


class Compra(models.Model):
	num_compra = models.IntegerField(default=0)
	status = models.BooleanField(default=False)
	total = models.DecimalField(decimal_places=2, max_digits=10)
	proveedor = models.ForeignKey(Proveedor,null=True)

	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __str__(self):
		return str(self.pk)


class DetalleCompra(models.Model):
	material = models.ForeignKey('inventario.Material', null=True)
	cantidad = models.IntegerField(default=0)
	precio = models.DecimalField(decimal_places=2, max_digits=10)

	compra = models.ForeignKey(Compra,null=True)

	@property
	def subtotal(self):
		return self.cantidad * self.precio
	

	def __str__(self):
		return str(self.compra)
    

class ContactoProveedor(models.Model):
	nombre = models.CharField(null=False, max_length=100)
	puesto = models.CharField(null= False, max_length=30)
	telefono = models.CharField(null= False, max_length=20)
	correo = models.CharField(null= False, max_length=20)
	proveedor = models.ForeignKey(Proveedor,null=True)

	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)