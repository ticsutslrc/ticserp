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


def ClienteNuevo(request):
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







