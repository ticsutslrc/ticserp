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
    url(r'^borrar_proveedor/(?P<pk>\d+)/',views.borrar_proveedor, name = 'borrar_proveedor'),

    url(r'^compra$', views.CompraConsultar, name='compra_consultar'),
    url(r'^compra/alta$', views.CompraAlta, name='compra_alta'),
    #url(r'^compra/(?P<pk>[0-9]+)$', views.CompraModificar, name='compra_modificar'),
    url(r'^borrar_compra/(?P<pk>\d+)/',views.borrar_compra, name = 'borrar_compra'),


    url(r'^compradetalle/(?P<pk>\d+)$', views.CompraDetalle, name='compradetalle_consultar'),
    url(r'^compradetalle/alta/(?P<pk>\d+)$', views.DetalleCompraAlta, name='compradetalle_alta'),

    url(r'^contactoProveedor$', views.ContactoProveedorConsultar, name='ContactoProveedor_consultar'),
    url(r'^contactoProveedor/alta$', views.ContactoProveedorAlta, name='ContactoProveedor_alta'),
    url(r'^contactoProveedor/(?P<pk>[0-9]+)$', views.ContactoProveedorModificar, name='ContactoProveedor_modificar'),
    url(r'^borrar_contacto/(?P<pk>\d+)/',views.borrar_contacto, name = 'borrar_contacto'),

    url(r'^proveedoresreporte$', views.reporte_proveedores, name='proveedor_reporte'),
    url(r'^comprasreporte$', views.reporte_compras, name='compra_reporte'),
    url(r'^contactosreporte$', views.reporte_contactos, name='contacto_reporte'),
    url(r'^detallesreporte$', views.reporte_detalle_compra, name='detalles_reporte'),

]