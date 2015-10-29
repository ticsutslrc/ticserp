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
