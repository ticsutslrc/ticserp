# -*- coding: utf-8 -*-

from rest_framework import serializers

from inventario.models import Producto, Material, DetalleProductosMaterial, MovimientoInventarioProduto, MovimientoInventarioMaterial


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'nombre',)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        #fields = '__all__'


class DetalleProductosMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProductosMaterial
        #fields = '__all__'


class MovimientoInventarioProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventarioProduto
        #fields = '__all__'


class MovimientoInventarioMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventarioMaterial
        #fields = '__all__'
