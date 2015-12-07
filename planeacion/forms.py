__author__ = 'ADMIN'
from django.forms import ModelForm
from django.forms import forms
from . import models


class nuevaOrdenForm(ModelForm):
    class Meta:
        model = models.planeacion
        fields = [
            'id_lote',
            'id_venta',
            'nombre_articulo',
            'cantidad',
            'status',
            'fecha_inicio',
            'fecha_creacion',
            'fecha_entrega',
        ]


class status(ModelForm):
    class Meta:
        model = models.planeacion
        fields = [
            'status',
        ]




