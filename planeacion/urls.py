# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^index', views.nuevaOrden, name='nueva_orden'),
    url(r'^mostrar$', views.consultar, name='mostrar'),
    url(r'^cambiar_status/(?P<pk>[0-9]+)$', views.cambiar_status, name='cambiar_status'),
    url(r'^cambiar_status2/(?P<pk>[0-9]+)$', views.cambiar_status2, name='cambiar_status2'),
    url(r'^cambiar_status_venta/(?P<pk>[0-9]+)$', views.cambiar_status_venta, name='cambiar_status_venta'),
    url(r'^Reporte$', views.generar_pdf, name='generar_pdf'),

]
