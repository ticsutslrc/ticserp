# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
   	url(r'^proveedores$', views.ProveedorConsultar, name='proveedor_consultar'),
    url(r'^proveedores/alta$', views.ProveedorAlta, name='proveedor_alta'),
    url(r'^proveedores/(?P<pk>[0-9]+)$', views.ProveedorModificar, name='proveedor_modificar'),
]
