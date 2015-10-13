# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from . import forms
from . import models

# Create your views here.
def main(request):
    """
    Vista principal de modulo de inventarios
    """
    return render(request, 'inventario/index.html')


def ProductoConsultar(request):
    """
    Vista para consulatar productos
    """
    productos = models.Producto.objects.all()
    return render(request, 'inventario/productos/consultar.html', {'productos': productos})


def ProductoAlta(request):
    """
    Vista para dar de alta productos
    """
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            #
            messages.add_message(request, messages.INFO, 'Producto agregado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_consultar'))
        else:
            return render(request, 'inventario/productos/agregar.html', {'form': form})
    else:
        form = forms.ProductoForm()
    return render(request, 'inventario/productos/agregar.html', {'form': form})

def ProductoModificar(request, pk):
    """
    Vista para dar de modificar productos
    """
    producto = get_object_or_404(models.Producto, pk=pk)
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Producto modificado con exito')
            return HttpResponseRedirect(reverse('inventario:productos_consultar'))
        else:
            return render(request, 'inventario/productos/agregar.html', {'form': form})
    else:
        form = forms.ProductoForm(instance=producto)
    return render(request, 'inventario/productos/agregar.html', {'form': form})