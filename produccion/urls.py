# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^orden/(?P<pk>[0-9]+)$', views.ordenDetalle, name='detalle_orden'),
    url(r'^orden/(?P<pk>[0-9]+)/status/(?P<status>[0-9]+)$', views.cambiarStatus, name='cambiar_status'),
    url(r'^statsProduccion$', views.produccionStats, name='produccion_stats'),
]
