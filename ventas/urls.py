# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^clientes$', views.ClienteConsultar, name='clientes_consultar'),
    url(r'^clientes/nuevo$', views.ClienteNuevo, name='clientes_nuevo'),
    url(r'^clientes/(?P<pk>[0-9]+)$', views.ClienteEditar, name='clientes_editar'),
	url(r'^clientes/eliminar/(?P<pk>[0-9]+)$', views.ClienteEliminar, name='clientes_eliminar'),
]
