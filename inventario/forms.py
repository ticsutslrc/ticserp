# -*- coding: utf-8 -*-
from django.forms import ModelForm

from . import models

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = [
            'nombre',
            'descripccion',
            'numero_inventario',
            'codigo_barras',
            'peso',
            'ultimo_costo',
            'costo_promedio',
            'cantidad_total_almacen',
            'cantidad_minimo_almacen',
        ]
