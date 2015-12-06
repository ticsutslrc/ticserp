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

    url(r'^clientes/contacto$', views.ContactoClienteConsultar, name='contacto_clientes_consultar'),
    url(r'^clientes/contacto/alta$', views.ContactoClienteAlta, name='contacto_clientes_alta'),
    url(r'^clientes/contacto/(?P<pk>[0-9]+)$', views.ContactoClienteEditar, name='contacto_clientes_editar'),
    url(r'^clientes/contacto/eliminar/(?P<pk>[0-9]+)$', views.ContactoClienteEliminar, name='contacto_clientes_eliminar'),
    url(r'^clientes/contacto/reporte$', views.generar_pdf_contacto_clientes, name='contacto_clientes_reporte'),
    
    url(r'^ventas/$', views.VentaConsultar, name='ventas_consultar'),
    url(r'^ventas/alta$', views.VentaAlta, name='ventas_alta'),
    url(r'^ventas/eliminar/(?P<pk>\d+)/', views.VentaEliminar, name='ventas_eliminar'),
    url(r'^ventas/buscar$', views.VentaBuscar, name='ventas_buscar'),
    url(r'^ventas/reporte$', views.generar_pdf_ventas, name='ventas_reporte'),
    url(r'^ventas/detalle/reporte/(?P<slug>[-\w]+)/$', views.generar_pdf_detalle_venta, name='detalle_venta_reporte'),
    
]
