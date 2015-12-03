# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^agregar$', views.nuevaOrden, name='nueva_orden'),
    url(r'^mostrar$', views.consultar, name='mostrar'),
]
