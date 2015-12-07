from django.shortcuts import render, Http404
from planeacion import models

# Create your views here.
def main(request):
    """
    Vista principal
    """
    ordenes = models.planeacion.objects.all().order_by('-fecha_entrega')
    return render(request, 'produccion/index.html', {'ordenes': ordenes})

def ordenDetalle(request, pk):
    try:
        orden = models.planeacion.objects.get(id_lote=pk)
        materiales = orden.nombre_articulo.detalleproductosmaterial_set.all()
    except models.planeacion.DoesNotExist:
        raise Http404("esta orden no existe")
    return render(request, 'produccion/ordenDetalle.html', {'orden':orden, 'materiales':materiales})