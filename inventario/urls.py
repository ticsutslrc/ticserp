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
    url(r'^productos/(?P<pk>[0-9]+)$', views.productos_view, name='productos_view'),
    url(r'^productos/(?P<pk>[0-9]+)/modificar$', views.productos_edit, name='productos_edit'),
    url(r'^productos/(?P<pk>[0-9]+)/eliminar$', views.productos_delete, name='productos_delete'),
    url(r'^productos/(?P<pk>[0-9]+)/material/asignar$', views.productos_asign_material, name='productos_asignar_material'),
    url(r'^productos/(?P<pk>[0-9]+)/registrar/movimiento$', views.productos_registrar_movimiento, name='productos_registrar_movimiento'),
    url(r'^productos/(?P<pk>[0-9]+)/qr', views.productos_generar_qr, name='productos_generar_qr'),
    url(r'^productos/(?P<pk>[0-9]+)/chart', views.productos_chart, name='productos_chart'),

    url(r'^materiales$', views.materiales, name='materiales'),
    url(r'^materiales/agregar$', views.materiales_add, name='materiales_add'),
    url(r'^materiales/(?P<pk>[0-9]+)$', views.materiales_view, name='materiales_view'),
    url(r'^materiales/(?P<pk>[0-9]+)/modificar$', views.materiales_edit, name='materiales_edit'),
    url(r'^materiales/(?P<pk>[0-9]+)/eliminar$', views.materiales_delete, name='materiales_delete'),
    url(r'^materiales/(?P<pk>[0-9]+)/registrar/movimiento$', views.materiales_registrar_movimiento, name='materiales_registrar_movimiento'),
    url(r'^materiales/(?P<pk>[0-9]+)/qr', views.materiales_generar_qr, name='materiales_generar_qr'),
    url(r'^materiales/(?P<pk>[0-9]+)/chart', views.materiales_chart, name='materiales_chart'),
]
