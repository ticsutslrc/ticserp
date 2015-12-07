"""ticserp URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('mainapp.urls', namespace='mainapp')),
    url(r'^compras/', include('compras.urls', namespace='compras')),
    url(r'^inventario/', include('inventario.urls', namespace='inventario')),
    url(r'^planeaccion/', include('planeacion.urls', namespace='planeaccion')),
    url(r'^produccion/', include('produccion.urls', namespace='produccion')),
    url(r'^ventas/', include('ventas.urls', namespace='ventas')),
    url(r'^admin/', include(admin.site.urls)),
]
