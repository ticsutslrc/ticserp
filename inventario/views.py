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


def productos(request):
    query = models.Producto.objects.all()
    return render(request, 'inventario/productos.html', {'productos': query, })


def productos_add(request):
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Producto agregado con exito')
            return HttpResponseRedirect(reverse('inventario:productos'))
        else:
            return render(request, 'inventario/productos_add.html', {'form': form, })
    else:
        form = forms.ProductoForm()
    return render(request, 'inventario/productos_add.html', {'form': form, })


def materiales(request):
    query = models.Material.objects.all()
    return render(request, 'inventario/materiales.html', {'materiales': query, })


def materiales_add(request):
    if request.method == 'POST':
        form = forms.MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Material agregado con exito')
            return HttpResponseRedirect(reverse('inventario:materiales'))
        else:
            return render(request, 'inventario/materiales_add.html', {'form': form, })
    else:
        form = forms.MaterialForm()
    return render(request, 'inventario/materiales_add.html', {'form': form, })
