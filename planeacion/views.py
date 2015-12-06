from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import messages
from . import forms
from . import models
from ventas.models import Venta
from django.http import HttpResponse
#import reportes
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table




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
            return HttpResponseRedirect(reverse('planeaccion:nueva_orden'))
        else:
            return render(request, 'planeacion/cambiar_status2.html', {'form': form})
    else:
        form = forms.nuevaOrdenForm(instance=query)
    return render(request, 'planeacion/cambiar_status2.html', {'form': form})

def cambiar_status_venta(request, pk):
    query = get_object_or_404(Venta, pk=pk)
    query.planeacion=True
    query.save()
    messages.add_message(request, messages.INFO, 'Status de venta modificado')
    return HttpResponseRedirect(reverse('planeaccion:nueva_orden'))


def generar_pdf(request):
    print ("Generando el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "ordenesdeproduccion.pdf"

    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    orden = []
    styles = getSampleStyleSheet()
    header = Paragraph("Reporde de ordenes de produccion", styles['Heading1'])
    orden.append(header)
    headings = ('Lote','Venta','Articulo','Cantidad','Estatus','Fecha Inicio','Fecha creacion','Fecha de entrega')
    ordenes = [(p.id_lote,p.id_venta,p.nombre_articulo,p.cantidad,p.status,p.fecha_inicio,p.fecha_creacion) for p in models.planeacion.objects.all()]
    print (ordenes)

    t = Table([headings] + ordenes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.blue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    orden.append(t)
    doc.build(orden)
    response.write(buff.getvalue())
    buff.close()
    return response