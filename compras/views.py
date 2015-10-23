# -*- coding: utf-8 -*-
"""
Compras vistas
Aqui se van a poner todas las vistas de compras
"""
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from . import forms
from . import models


def main(request):
    """
    Vista principal de compras
    """
    return render(request, 'compras/index.html')

def ProveedorConsultar(request):
    """
    Vista para consulta de proveedores
    """
    proveedores = models.Proveedor.objects.all()
    return render(request, 'compras/proveedores/consultar.html', {'proveedores': proveedores})


def ProveedorAlta(request):
    """
    Vista para alta de proveedores
    """
    if request.method == 'POST':
        form = forms.ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            #
            messages.add_message(request, messages.INFO, 'Proveedor agregado con exito')
            return HttpResponseRedirect(reverse('compras:proveedor_consultar'))
        else:
            return render(request, 'compras/proveedores/agregar.html', {'form': form})
    else:
        form = forms.ProveedorForm()
    return render(request, 'compras/proveedores/agregar.html', {'form': form})

def ProveedorModificar(request, pk):
    """
    Vista para modificar proveedor
    """
    proveedor = get_object_or_404(models.Proveedor, pk=pk)
    if request.method == 'POST':
        form = forms.ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Proveedor modificado con exito')
            return HttpResponseRedirect(reverse('compras:proveedor_consultar'))
        else:
            return render(request, 'compras/proveedores/agregar.html', {'form': form})
    else:
        form = forms.ProveedorForm(instance=proveedor)
    return render(request, 'compras/proveedores/agregar.html', {'form': form})
