# -*- coding: utf-8 -*-

from django.forms import ModelForm

from . import models

class ClienteForm(ModelForm):
    class Meta:
        model = models.Cliente
        fields = [
            'nombre',
            'rfc',
            'direccion',
            'ciudad',
            'estado',
            'pais',
            'giro',
            'telefono',
            'correo',
        ]


class VentaForm(ModelForm):
    class Meta:
        model = models.Venta
        fields = [
            'num_factura',
            'cliente'
        ]


class DetalleVentaProductoForm(ModelForm):
    class Meta:
        model = models.DetalleVenta
        fields = [
            'producto',
            'precio',
            'cantidad'
        ] 
        exclude = ['venta']
    
