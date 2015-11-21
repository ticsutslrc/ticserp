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
    url(r'^clientes/reporte$', views.generar_pdf_clientes, name='clientes_reporte'),
    
    url(r'^ventas/$', views.VentaConsultar, name='ventas_consultar'),
    url(r'^ventas/alta$', views.VentaAlta, name='ventas_alta'),
    url(r'^ventas/detalle/(?P<pk>\d+)/', views.VentaDetalle, name='ventas_detalle'),
    url(r'^ventas/agregar_producto/(?P<pk>\d+)/', views.AgregarProductoDetalleVenta, name='agregar_producto'),
    url(r'^ventas/reporte/(?P<pk>\d+)/', views.generar_pdf_ventas, name='ventas_reporte'),

    url(r'^ventas/eliminar/(?P<pk>\d+)/', views.VentaEliminar, name='ventas_eliminar'),
    url(r'^ventas/agregar_producto/eliminar/(?P<pk>\d+)/', views.DetalleVentaEliminar, name='detalleventa_eliminar'),

]
