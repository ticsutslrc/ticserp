# -*- coding: utf-8 -*-

from django.forms import ModelForm

from . import models

class ProveedorForm(ModelForm):
    class Meta:
        model = models.Proveedor
        fields = [
            'num_proveedor',
            'nombre',
            'RFC',
            'giro',
            'direccion',
            'ciudad',
            'estado',
            'pais',
            'telefono',
            'correo',
            'comentario',
        ]


class CompraForm(ModelForm):
    class Meta:
        model = models.Compra
        fields = [
            'num_compra',
            'status',
            'total',
            'proveedor',

        ]


class DetalleCompraForm(ModelForm):
    class Meta:
        model = models.DetalleCompra
        fields = [
            'material',
            'precio',
            'cantidad'
        ] 
        exclude = ['compra']


class ContactoProveedorForm(ModelForm):
    class Meta:
        model = models.ContactoProveedor      
        fields = [
        'nombre',
        'puesto',
        'telefono',
        'correo',
        'proveedor',
        ]