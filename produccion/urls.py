# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^orden/(?P<pk>[0-9]+)$', views.ordenDetalle, name='detalle_orden'),
]
