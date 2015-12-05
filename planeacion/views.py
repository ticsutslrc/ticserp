from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import messages
from . import forms
from . import models
from ventas.models import Venta

#from ventas import models

# Create your views here.
def main(request):

    return render(request, 'planeacion/main.html')



def nuevaOrden(request):
    planeacion = models.planeacion.objects.all()
    if request.method == 'POST':
        form = forms.nuevaOrdenForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'orden agregada')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'planeacion/index.html', {'form': form})
    else:
        form = forms.nuevaOrdenForm()
    return render(request, 'planeacion/index.html', {'form': form, 'planeacion': planeacion})


def consultar(request):
    planeacion = models.planeacion.objects.all()
    ventas = get_object_or_404(Venta, planeacion=False)

    return render(request, 'planeacion/mostrar.html', {'planeacion': planeacion,'ventas': ventas})



def cambiar_status(request, pk):
    query = get_object_or_404(models.planeacion, pk=pk)

    return render(request, 'planeacion/cambiar_status.html', {'consulta': query})

def cambiar_status2(request, pk):

    query = get_object_or_404(models.planeacion, pk=pk)
    if request.method == 'POST':
        form = forms.status(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Status modificado')
            return HttpResponseRedirect(reverse('planeaccion:main'))
        else:
            return render(request, 'planeacion/cambiar_status2.html', {'form': form})
    else:
        form = forms.nuevaOrdenForm(instance=query)
    return render(request, 'planeacion/cambiar_status2.html', {'form': form})

def crear_orden_produccion(request, factura, producto, cantidad):

    return render_to_response('ddd')








