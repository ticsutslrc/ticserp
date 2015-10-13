from django.db import models

# Create your models here.
class Venta(models.Model):
    total = models.DecimalField(decimal_places=4, max_digits=10)
    subtotal = models.DecimalField(decimal_places=4, max_digits=10)
    impuestos = models.DecimalField(decimal_places=4, max_digits=10)
    productos = models.ManyToManyField('inventario.Producto')

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)