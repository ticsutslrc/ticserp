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
    url(r'^compra$', views.CompraConsultar, name='compra_consultar'),
    url(r'^compra/alta$', views.CompraAlta, name='compra_alta'),
    url(r'^compra/(?P<pk>[0-9]+)$', views.CompraModificar, name='compra_modificar'),
    url(r'^contactoProveedor$', views.ContactoProveedorConsultar, name='ContactoProveedor_consultar'),
    url(r'^contactoProveedor/alta$', views.ContactoProveedorAlta, name='ContactoProveedor_alta'),
    url(r'^contactoProveedor/(?P<pk>[0-9]+)$', views.ContactoProveedorModificar, name='ContactoProveedor_modificar'),
    url(r'^reporteproveedores/$', views.generar_pdf, name='reporteproveedores'),
]