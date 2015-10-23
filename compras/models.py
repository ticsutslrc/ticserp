# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(null=False, max_length=100)
	responsable = models.CharField(null=True, blank=True, max_length=50)
	direccion = models.CharField(null=False, max_length=50)
	ciudad = models.CharField(null= False, max_length=30)
	estado = models.CharField(null= False, max_length=30)
	pais = models.CharField(null= False, max_length=30)
	telefono = models.CharField(null= False, max_length=20)
	correo = models.CharField(null= False, max_length=20)
	
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)