# -*- coding: utf-8 -*-
from django.forms import ModelForm

from . import models

class ClienteForm(ModelForm):
    class Meta:
        model = models.Cliente
        fields = [
            'nombre',
            'compania',
            'direccion',
            'ubicacion',
            'telefono',
            'correo',
        ]
