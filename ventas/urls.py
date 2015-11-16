# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^clientes$', views.ClienteConsultar, name='clientes_consultar'),
    url(r'^clientes/alta$', views.ClienteAlta, name='clientes_alta'),
    url(r'^clientes/(?P<pk>[0-9]+)$', views.ClienteEditar, name='clientes_editar'),
    url(r'^clientes/eliminar/(?P<pk>[0-9]+)$', views.ClienteEliminar, name='clientes_eliminar'),
    
    url(r'^ventas$', views.VentaConsultar, name='ventas_consultar'),
    url(r'^ventas/alta$', views.VentaAlta, name='ventas_alta'),
    url(r'^ventas/detalle/(?P<pk>\d+)/', views.VentaDetalle, name='ventas_detalle'),
    url(r'^ventas/agregar_producto/(?P<pk>\d+)/', views.DetalleVentaProducto, name='agregar_producto'),

]
