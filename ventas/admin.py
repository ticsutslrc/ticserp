# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Cliente
from .models import Venta
from .models import DetalleVenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
