# -*- coding: utf-8 -*-

from django.forms import ModelForm

from . import models

class ProveedorForm(ModelForm):
    class Meta:
        model = models.Proveedor
        fields = [
            'nombre',
            'direccion',
            'ciudad',
            'estado',
            'pais',
            'telefono',
            'correo',
        ]
