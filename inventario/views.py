# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from rest_framework import viewsets

from .serializers import ProductoSerializer
from .serializers import MaterialSerializer
from .serializers import DetalleProductosMaterialSerializer
from .serializers import MovimientoInventarioProdutoSerializer
from .serializers import MovimientoInventarioMaterialSerializer
from .models import Producto
from .models import Material
from .models import DetalleProductosMaterial
from .models import MovimientoInventarioProduto
from .models import MovimientoInventarioMaterial

# Create your views here.
def main(request):
    """
    Vista principal de modulo de inventarios
    """
    return render(request, 'inventario/index.html')


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class DetalleProductosMaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DetalleProductosMaterial.objects.all()
    serializer_class = DetalleProductosMaterialSerializer


class MovimientoInventarioProdutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MovimientoInventarioProduto.objects.all()
    serializer_class = MovimientoInventarioProdutoSerializer


class MovimientoInventarioMaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MovimientoInventarioProduto.objects.all()
    serializer_class = MovimientoInventarioMaterialSerializer