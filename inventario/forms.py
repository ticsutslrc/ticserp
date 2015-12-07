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
            'cantidad_total_almacen',
            'cantidad_minimo_almacen',
            'comentarios',
        ]


class MaterialForm(ModelForm):
    class Meta:
        model = models.Material
        fields = [
            'proveedor',
            'nombre',
            'descripccion',
            'numero_inventario',
            'codigo_barras',
            'peso',
            'ultimo_costo',
            'cantidad_total_almacen',
            'cantidad_minimo_almacen',
            'comentarios',
        ]


class DetalleProductoMaterial(ModelForm):
    class Meta:
        model = models.DetalleProductosMaterial
        fields = [
            'material',
            'cantidad',
            'comentarios',
        ]


class MovimeintoInventarioProducto(ModelForm):
    class Meta:
        model = models.MovimientoInventarioProduto
        fields = [
            'tipo',
            'cantidad',
            'comentarios',
        ]


class MovimientoInventarioMaterial(ModelForm):
    class Meta:
        model = models.MovimientoInventarioMaterial
        fields = [
            'tipo',
            'cantidad',
            'comentarios',
        ]