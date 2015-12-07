# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib import messages

from . import forms
from . import models


# Create your views here.
def main(request):
    """
    Vista principal de modulo de inventarios
    """
    return render(request, 'inventario/index.html')


def productos(request):
    query = models.Producto.objects.all()
    return render(request, 'inventario/productos.html', {'productos': query, })


def productos_add(request):
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Producto agregado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_view', args=[form.id]))
        else:
            return render(request, 'inventario/productos_add.html', {'form': form, })
    else:
        form = forms.ProductoForm()
    return render(request, 'inventario/productos_add.html', {'form': form, })


def productos_edit(request, pk):
    producto = get_object_or_404(models.Producto, pk=pk)
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Producto modificado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_view', args=[form.pk]))
        else:
            return render(request, 'inventario/productos_add.html', {'form': form, 'producto': producto, })
    else:
        form = forms.ProductoForm(instance=producto)
    return render(request, 'inventario/productos_add.html', {'form': form, 'producto': producto, })


def productos_view(request, pk):
    producto = get_object_or_404(models.Producto, pk=pk)
    movimiento_inventario = producto.movimientoinventarioproduto_set.all()
    materiales = producto.detalleproductosmaterial_set.all()
    return render(request, 'inventario/productos_view.html', {
        'producto': producto,
        'movimiento_inventario': movimiento_inventario,
        'materiales': materiales,
    })


def productos_delete(request, pk):
    producto = get_object_or_404(models.Producto, pk=pk)
    producto.delete()
    messages.add_message(request, messages.INFO, 'Producto borrado {0}'.format(producto.nombre))
    return HttpResponseRedirect(reverse('inventario:productos'))


def productos_asign_material(request, pk):
    producto = get_object_or_404(models.Producto, pk=pk)
    detalle_producto_material = models.DetalleProductosMaterial()
    detalle_producto_material.producto = producto
    if request.method == 'POST':
        form = forms.DetalleProductoMaterial(request.POST, instance=detalle_producto_material)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Detalle material agregado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_view', args=[producto.pk]))
        else:
            return render(request, 'inventario/productos_asign_material.html', {'form': form, 'producto': producto, })
    else:
        form = forms.DetalleProductoMaterial(instance=detalle_producto_material)
    return render(request, 'inventario/productos_asign_material.html', {'form': form, 'producto': producto, })


def productos_registrar_movimiento(request, pk):
    producto = get_object_or_404(models.Producto, pk=pk)
    movimiento = models.MovimientoInventarioProduto()
    movimiento.producto = producto
    if request.method == 'POST':
        form = forms.MovimeintoInventarioProducto(request.POST, instance=movimiento)
        if form.is_valid():

            cant = form.cleaned_data['cantidad']
            tipo = form.cleaned_data['tipo']
            comentarios = form.cleaned_data['comentarios']

            if tipo == models.TIPO_MOVIMIENTO_ENTRADA:
                producto.entrada_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_SALIDA:
                producto.salida_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_REMISION:
                producto.remision_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_AJUSTE:
                producto.ajuste_inventario(cant, comentarios=comentarios)

            messages.add_message(request, messages.INFO, 'Movimiento registrado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_view', args=[producto.pk]))
        else:
            return render(request, 'inventario/productos_registrar_movimientos.html',
                          {'form': form, 'producto': producto, })
    else:
        form = forms.MovimeintoInventarioProducto(instance=movimiento)
    return render(request, 'inventario/productos_registrar_movimientos.html', {'form': form, 'producto': producto, })


def materiales_json(request):
    query = models.Material.objects.all()
    json_data = serializers.serialize('json', query)
    return HttpResponse(json_data, content_type="application/json")


def materiales(request):
    query = models.Material.objects.all()
    return render(request, 'inventario/materiales.html', {'materiales': query, })


def materiales_add(request):
    if request.method == 'POST':
        form = forms.MaterialForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Material agregado con exito')
            return HttpResponseRedirect(reverse('inventario:materiales_view', args=[form.pk]))
        else:
            return render(request, 'inventario/materiales_add.html', {'form': form, })
    else:
        form = forms.MaterialForm()
    return render(request, 'inventario/materiales_add.html', {'form': form, })


def materiales_edit(request, pk):
    material = get_object_or_404(models.Material, pk=pk)
    if request.method == 'POST':
        form = forms.MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Material modificado con exito')
            return HttpResponseRedirect(reverse('inventario:materiales_view', args=[form.pk]))
        else:
            return render(request, 'inventario/materiales_add.html', {'form': form, 'material': material, })
    else:
        form = forms.MaterialForm(instance=material)
    return render(request, 'inventario/materiales_add.html', {'form': form, 'material': material, })


def materiales_view(request, pk):
    material = get_object_or_404(models.Material, pk=pk)
    movimiento_inventario = material.movimientoinventariomaterial_set.all()
    productos = material.detalleproductosmaterial_set.all()
    return render(request, 'inventario/materiales_view.html', {
        'material': material,
        'movimiento_inventario': movimiento_inventario,
        'productos': productos,
    })


def materiales_delete(request, pk):
    material = get_object_or_404(models.Material, pk=pk)
    material.delete()
    messages.add_message(request, messages.INFO, 'Material borrado {0}'.format(material.nombre))
    return HttpResponseRedirect(reverse('inventario:materiales'))


def materiales_registrar_movimiento(request, pk):
    material = get_object_or_404(models.Material, pk=pk)
    movimiento = models.MovimientoInventarioMaterial()
    movimiento.material = material
    if request.method == 'POST':
        form = forms.MovimientoInventarioMaterial(request.POST, instance=movimiento)
        if form.is_valid():

            cant = form.cleaned_data['cantidad']
            tipo = form.cleaned_data['tipo']
            comentarios = form.cleaned_data['comentarios']

            if tipo == models.TIPO_MOVIMIENTO_ENTRADA:
                material.entrada_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_SALIDA:
                material.salida_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_REMISION:
                material.remision_inventario(cant, comentarios=comentarios)
            elif tipo == models.TIPO_MOVIMIENTO_AJUSTE:
                material.ajuste_inventario(cant, comentarios=comentarios)

            messages.add_message(request, messages.INFO, 'Movimiento registrado con exito')
            return HttpResponseRedirect(reverse('inventario:materiales_view', args=[material.pk]))
        else:
            return render(request, 'inventario/materiales_registrar_movimientos.html',
                          {'form': form, 'material': material, })
    else:
        form = forms.MovimientoInventarioMaterial(instance=movimiento)
    return render(request, 'inventario/materiales_registrar_movimientos.html', {'form': form, 'material': material, })