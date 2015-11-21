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
from .models import DetalleVenta

from django.db.models import Sum
from django.db.models import F

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
        total = models.DetalleVenta.objects.filter(venta=pk).aggregate(total=Sum(F('precio') * F('cantidad')))['total']
    except models.Venta.DoesNotExist:
        raise Http404('Este detalle no existe')
    return render(request, 'ventas/ventas/detalle.html', {'detalles' : detalles,'venta' : venta,'total' : total})

def AgregarProductoDetalleVenta(request, pk):
    if request.method == 'POST':
        venta = models.Venta.objects.get(pk=pk)
        form = forms.DetalleVentaProductoForm(request.POST)
        if form.is_valid():
            ventaproducto = form.save(commit=False)
            ventaproducto.venta = venta
            ventaproducto.save()            
            venta = models.Venta.objects.get(pk=pk)
            detalles = venta.detalleventa_set.all()
            total = models.DetalleVenta.objects.filter(venta=pk).aggregate(total=Sum(F('precio') * F('cantidad')))['total']
            return render(request, 'ventas/ventas/agregar_producto.html', {'form': form,'detalles' : detalles,'venta' : venta,'total' : total})
        else:
            return render(request, 'ventas/ventas/agregar_producto.html', {'form': form,'detalles' : detalles,'venta' : venta,'total' : total})
    else:
        form = forms.DetalleVentaProductoForm()
        venta = models.Venta.objects.get(pk=pk)
        detalles = venta.detalleventa_set.all()
        total = models.DetalleVenta.objects.filter(venta=pk).aggregate(total=Sum(F('precio') * F('cantidad')))['total']
    return render(request, 'ventas/ventas/agregar_producto.html', {'form': form,'detalles' : detalles,'venta' : venta,'total' : total})


def VentaEliminar(request, pk):
    venta = get_object_or_404(models.Venta, pk=pk)
    venta.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def DetalleVentaEliminar(request, pk):
    detalle = get_object_or_404(models.DetalleVenta, pk=pk)
    detalle.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


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



def generar_pdf_ventas(request,pk):
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
    header = Paragraph("Venta - Detalle", styles['Heading1'])
    ventas.append(header)


    datosVenta = models.Venta.objects.get(pk=pk)
    numeroVenta = Paragraph("NUMERO VENTA: " + str(datosVenta.num_factura), styles['Heading3'])
    ventas.append(numeroVenta)

    clienteVenta = Paragraph("CLIENTE: " + str(datosVenta.cliente), styles['Heading3'])
    ventas.append(clienteVenta)

    fechaVenta = Paragraph("FECHA: " + str(datosVenta.fecha), styles['Heading3'])
    ventas.append(fechaVenta)


    headings = ('Producto','Cantidad','Precio','SubTotal')
    allventas = [(p.producto, p.cantidad, p.precio, p.subtotal) for p in DetalleVenta.objects.filter(venta=pk)]
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


    datoTotal = models.DetalleVenta.objects.filter(venta=pk).aggregate(total=Sum(F('precio') * F('cantidad')))['total']
    totalVenta = Paragraph("TOTAL: " + str(datoTotal), styles['Heading3'])
    ventas.append(totalVenta)


    doc.build(ventas)
    response.write(buff.getvalue())
    buff.close()
    return response