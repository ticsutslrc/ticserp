# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'MovimientoInventarioProdutoViewSet', views.MovimientoInventarioProdutoViewSet)
router.register(r'MovimientoInventarioMaterialViewSet', views.MovimientoInventarioMaterialViewSet)
router.register(r'DetalleProductosMaterial', views.DetalleProductosMaterialViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'materiales', views.MaterialViewSet)

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^api/', include(router.urls)),
]
