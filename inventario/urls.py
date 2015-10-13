# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^productos$', views.ProductoConsultar, name='productos_consultar'),
    url(r'^productos/alta$', views.ProductoAlta, name='productos_alta'),
    url(r'^productos/(?P<pk>[0-9]+)$', views.ProductoModificar, name='productos_modificar'),
]
