from django.shortcuts import render, Http404
from planeacion import models
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main(request):
    """
    Vista principal
    """
    #filter(id_venta__planeacion = True)
    ordenes_iniciadas = models.planeacion.objects.filter(status=2).order_by('-fecha_entrega')
    ordenes_sininiciar = models.planeacion.objects.filter(status=3).order_by('-fecha_entrega')
    ordenes_canceladas = models.planeacion.objects.filter(status=1).order_by('-fecha_entrega')
    return render(request, 'produccion/index.html', {'ordenes': ordenes_iniciadas, 'ordenes_sininiciar': ordenes_sininiciar, 'ordenes_canceladas': ordenes_canceladas})

@login_required
def ordenDetalle(request, pk):
    try:
        orden = models.planeacion.objects.get(id_lote=pk)
        materiales = orden.nombre_articulo.detalleproductosmaterial_set.all()
    except models.planeacion.DoesNotExist:
        raise Http404("esta orden no existe")
    return render(request, 'produccion/ordenDetalle.html', {'orden':orden, 'materiales':materiales})

@login_required
def cambiarStatus(request, pk, status):
    try:
        orden = models.planeacion.objects.get(id_lote=pk)
        orden.status = status
        if(status == 4):
            orden.id_venta.produccion = True
            messages.add_message(request, messages.SUCCESS, 'Orden terminada : Orden # ' + str(orden.id_lote))

        orden.save()
        materiales = orden.nombre_articulo.detalleproductosmaterial_set.all()
        messages.add_message(request, messages.INFO, 'Status Modificado : Orden # ' + str(orden.id_lote))

    except models.planeacion.DoesNotExist:
        raise Http404("esta orden no existe")
    return render(request, 'produccion/ordenDetalle.html',{'orden':orden, 'materiales':materiales})

