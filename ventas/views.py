# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404

from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from . import forms
from . import models
from .models import Cliente

from django.db.models import Sum
from django.db.models import F

# Create your views here.
def main(request):
    """
    Vista principal
    """
    return render(request, 'ventas/index.html')


# Vista para agregar clientes
def ClienteAlta(request):
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


# Vista para consultar clientes
def ClienteConsultar(request):
    clientes = models.Cliente.objects.all()
    return render(request, 'ventas/clientes/consultar.html', {'clientes' : clientes})


# Vista para editar clientes
def ClienteEditar(request, pk):
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


# Vista para eliminar clientes
def ClienteEliminar(request, pk):
    cliente = get_object_or_404(models.Cliente, pk=pk)
    cliente.delete()
    return HttpResponseRedirect(reverse('ventas:clientes_consultar'))


# Vista para agregar ventas
def VentaAlta(request):
    if request.method == 'POST':
        form = forms.VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            messages.add_message(request, messages.INFO, 'Venta agregada con exito')
            return HttpResponseRedirect(reverse('ventas:ventas_consultar'))
        else:
            return render(request, 'ventas/ventas/agregar.html', {'form': form})
    else:
        form = forms.VentaForm()
    return render(request, 'ventas/ventas/agregar.html', {'form': form})


# Vista para consultar ventas
def VentaConsultar(request):
    ventas = models.Venta.objects.all()
    return render(request, 'ventas/ventas/consultar.html', {'ventas' : ventas})


# Vista para eliminar ventas
def VentaEliminar(request, pk):
    venta = get_object_or_404(models.Venta, pk=pk)
    venta.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


# Vista para generar reporte de clientes
def generar_pdf_clientes(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado De Clientes", styles['Heading1'])
    clientes.append(header)
    headings = ('Nombre','RFC','Direccion','Ciudad','Estado','Pais','Giro','Correo','Telefono')
    allclientes = [(p.nombre, p.rfc, p.direccion, p.ciudad, p.estado, p.pais, p.giro, p.correo, p.telefono) for p in Cliente.objects.all()]
    print (allclientes);

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response


# Vista para generar reporte de ventas
def generar_pdf_ventas(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "ventas.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    ventas = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado De ventas", styles['Heading1'])
    ventas.append(header)
    headings = ('Num. Factura','Cliente','Fecha','Producto','Cantidad','Precio','Total')
    allventas = [(p.num_factura, p.cliente, p.fecha.strftime("%d-%m-%Y"), p.producto.nombre, p.cantidad, p.precio, p.total) for p in models.Venta.objects.all()]
    print (allventas);

    t = Table([headings] + allventas)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    ventas.append(t)
    doc.build(ventas)
    response.write(buff.getvalue())
    buff.close()
    return response