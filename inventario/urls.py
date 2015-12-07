# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^productos$', views.productos, name='productos'),
    url(r'^productos/agregar$', views.productos_add, name='productos_add'),
    url(r'^materiales$', views.materiales, name='materiales'),
    url(r'^materiales/agregar$', views.materiales_add, name='materiales_add'),
]
