from django.db import models



class planeacion(models.Model):
    id_lote = models.AutoField(primary_key=True)#id 
    id_venta = models.CharField(max_length=100)#id venta
    nombre_articulo = models.CharField(max_length=100)#relacion con articulo
    cantidad = models.IntegerField()
    status = models.CharField(max_length=15, choices=(
        ('1', 'Cancelado'),
        ('2', 'Iniciado'),
        ('3', 'Sin iniciar'),
    ), default='3')
    fecha_inicio = models.DateTimeField()
    fecha_creacion = models.DateTimeField()#auto
    fecha_entrega = models.DateTimeField()






