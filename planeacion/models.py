from django.db import models


# Create your models here.
class planeacion(models.Model):
    id_lote = models.CharField(max_length=30)
    nombre_articulo = models.CharField(max_length=100)
    piezas = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    progreso = models.CharField(max_length=30)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    fecha_terminacion = models.DateTimeField()



class modelos(models.Model):
    id_modelo = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    piezas = models.CharField(max_length=30)


