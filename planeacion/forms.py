__author__ = 'ADMIN'
from django.forms import ModelForm
from django.forms import forms
from . import models

class nuevaOrdenForm(ModelForm):
    class Meta:
        model = models.planeacion
        fields = [
            'id_lote',
            'nombre_articulo',
            'piezas',
            'cantidad',
            'status',
            'progreso',
            'fecha_inicio',
            'fecha_fin',
            'fecha_terminacion',
        ]

