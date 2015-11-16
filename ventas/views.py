# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404

from . import forms
from . import models

# Create your views here.
def main(request):
    """
    Vista principal
    """
    return render(request, 'ventas/index.html')


def ClienteAlta(request):
    """
    Vista para agregar nuevos clientes
    """
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Cliente agregado con exito')
            return HttpResponseRedirect(reverse('ventas:clientes_consultar'))
        else:
            return render(request, 'ventas/clientes/agregar.html', {'form': form})
    else:
        form = forms.ClienteForm()
    return render(request, 'ventas/clientes/agregar.html', {'form': form})


def ClienteConsultar(request):
    """
    Vista para consultar clientes
    """
    clientes = models.Cliente.objects.all()
    return render(request, 'ventas/clientes/consultar.html', {'clientes' : clientes})


def ClienteEditar(request, pk):
    """
    Vista para editar clientes
    """
    cliente = get_object_or_404(models.Cliente, pk=pk)
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Cliente modificado con exito')
            return HttpResponseRedirect(reverse('ventas:clientes_consultar'))
        else:
            return render(request, 'ventas/clientes/agregar.html', {'form': form})
    else:
        form = forms.ClienteForm(instance=cliente)
    return render(request, 'ventas/clientes/agregar.html', {'form': form})

def ClienteEliminar(request, pk):
    """
    Vista para eliminar clientes
    """
    cliente = get_object_or_404(models.Cliente, pk=pk)
    cliente.delete()
    return HttpResponseRedirect(reverse('ventas:clientes_consultar'))

def VentaAlta(request):
    if request.method == 'POST':
        form = forms.VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            return HttpResponseRedirect(reverse('ventas:agregar_producto', args=(venta.pk,)))
        else:
            return render(request, 'ventas/ventas/agregar.html', {'form': form})
    else:
        form = forms.VentaForm()
    return render(request, 'ventas/ventas/agregar.html', {'form': form})

def VentaConsultar(request):
    ventas = models.Venta.objects.all()
    return render(request, 'ventas/ventas/consultar.html', {'ventas' : ventas})

def VentaDetalle(request, pk):
    try:
        venta = models.Venta.objects.get(pk=pk)
        detalles = venta.detalleventa_set.all()
    except models.Venta.DoesNotExist:
        raise Http404('Este detalle no existe')
    return render(request, 'ventas/ventas/detalle.html', {'detalles' : detalles,'venta' : venta})

def DetalleVentaProducto(request, pk):
    if request.method == 'POST':
        venta = models.Venta.objects.get(pk=pk)
        form = forms.DetalleVentaProductoForm(request.POST)
        if form.is_valid():
            ventaproducto = form.save(commit=False)
            ventaproducto.venta = venta
            ventaproducto.save()            
            venta = models.Venta.objects.get(pk=pk)
            detalles = venta.detalleventa_set.all()
            return render(request, 'ventas/ventas/agregar_producto.html', {'form': form,'detalles' : detalles,'venta' : venta})
        else:
            return render(request, 'ventas/ventas/agregar_producto.html', {'form': form,'detalles' : detalles,'venta' : venta})
    else:
        form = forms.DetalleVentaProductoForm()
    return render(request, 'ventas/ventas/agregar_producto.html', {'form': form})