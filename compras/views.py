# -*- coding: utf-8 -*-
"""
Compras vistas
Aqui se van a poner todas las vistas de compras
"""
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,legal,landscape
from reportlab.platypus import Table
from . import forms
from . import models
from .models import Proveedor,Compra,ContactoProveedor,DetalleCompra


def main(request):
    """
    Vista principal de compras
    """
    return render(request, 'compras/index.html')


########################################### Proveedor ###########################################
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

def borrar_proveedor(request, pk):
    Proveedor.objects.get(pk=pk).delete()
    return ProveedorConsultar(request)


########################################### Compra ###########################################
def CompraConsultar(request):
    """
    Vista padef borrar_articulo(request, id):
    Articulo.objects.get(id=id).delete()
    return listado(request)ra consulta de proveedores
    """
    compras = models.Compra.objects.all()
    return render(request, 'compras/compra/consultar.html', {'compras': compras})


def CompraAlta(request):
    """
    Vista para alta de proveedores
    """
    if request.method == 'POST':
        form = forms.CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.add_message(request, messages.INFO, 'Compra agregada con exito')
            return HttpResponseRedirect(reverse('compras:compradetalle_alta', args=(compra.pk,)))
        else:
            return render(request, 'compras/compra/agregar.html', {'form': form})
    else:
        form = forms.CompraForm()
    return render(request, 'compras/compra/agregar.html', {'form': form})


def CompraModificar(request, pk):
    """
    Vista para modificar compra
    """
    compra = get_object_or_404(models.Compra, pk=pk)
    if request.method == 'POST':
        form = forms.CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Compra modificada con exito')
            return HttpResponseRedirect(reverse('compras:compra_consultar'))
        else:
            return render(request, 'compras/compra/agregar.html', {'form': form})
    else:
        form = forms.CompraForm(instance=compra)
    return render(request, 'compras/compra/agregar.html', {'form': form}) 

def borrar_compra(request, pk):
    Compra.objects.get(pk=pk).delete()
    return CompraConsultar(request)


########################################### Detalle Compra ###########################################
def CompraDetalle(request, pk):
    try:
        compra = models.Compra.objects.get(pk=pk)
        detalles = compra.detallecompra_set.all()
    except models.Compra.DoesNotExist:
        raise Http404('Este detalle no existe')
    return render(request, 'compras/detalleCompra/consultar.html', {'detalles' : detalles,'compra' : compra})


def DetalleCompraAlta(request, pk):
    if request.method == 'POST':
        compra = models.Compra.objects.get(pk=pk)
        form = forms.DetalleCompraForm(request.POST)
        if form.is_valid():
            ventaproducto = form.save(commit=False)
            ventaproducto.compra= compra
            ventaproducto.save()            
            compra = models.Compra.objects.get(pk=pk)
            detalles = compra.detallecompra_set.all()
            return render(request, 'compras/detalleCompra/agregar.html', {'form': form,'detalles' : detalles,'compra' : compra})
        else:
            return render(request, 'compras/detalleCompra/agregar.html', {'form': form,'detalles' : detalles,'compra' : compra})
    else:
        form = forms.DetalleCompraForm()
    return render(request, 'compras/detalleCompra/agregar.html', {'form': form})




########################################### Contacto Proveedor ###########################################
def ContactoProveedorConsultar(request):
    """
    Vista para consulta de proveedores
    """
    ContactoProveedores = models.ContactoProveedor.objects.all()
    return render(request, 'compras/contactoProveedor/consultar.html', {'ContactoProveedores': ContactoProveedores})


def ContactoProveedorAlta(request):
    """
    Vista para alta de proveedores
    """
    if request.method == 'POST':
        form = forms.ContactoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            #
            messages.add_message(request, messages.INFO, 'Compra agregada con exito')
            return HttpResponseRedirect(reverse('compras:ContactoProveedor_consultar'))
        else:
            return render(request, 'compras/contactoProveedor/agregar.html', {'form': form})
    else:
        form = forms.ContactoProveedorForm()
    return render(request, 'compras/contactoProveedor/agregar.html', {'form': form})


def ContactoProveedorModificar(request, pk):
    """
    Vista para modificar compra
    """
    ContactoProveedor = get_object_or_404(models.ContactoProveedor, pk=pk)
    if request.method == 'POST':
        form = forms.ContactoProveedorForm(request.POST, instance=ContactoProveedor)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Compra modificada con exito')
            return HttpResponseRedirect(reverse('compras:ContactoProveedor_consultar'))
        else:
            return render(request, 'compras/contactoProveedor/agregar.html', {'form': form})
    else:
        form = forms.ContactoProveedorForm(instance=ContactoProveedor)
    return render(request, 'compras/contactoProveedor/agregar.html', {'form': form})

def borrar_contacto(request, pk):
    ContactoProveedor.objects.get(pk=pk).delete()
    return ContactoProveedorConsultar(request)


########################################### Reportes ###########################################
def reporte_proveedores(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "proveedores.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=landscape(legal),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    proveedores = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Proveedores", styles['Heading1'])
    proveedores.append(header)
    headings = ('No. Proveedor','Nombre','RFC','Giro','Direccion','Ciudad','Estado','Pais','Telefono','Correo','Comentario')
    allproveedores = [(p.num_proveedor, p.nombre, p.RFC ,p.giro ,p.direccion ,p.ciudad ,p.estado ,p.pais ,p.telefono ,p.correo ,p.comentario) for p in Proveedor.objects.all()]
    print (allproveedores);

    t = Table([headings] + allproveedores)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    proveedores.append(t)
    doc.build(proveedores)
    response.write(buff.getvalue())
    buff.close()
    return response

def reporte_compras(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "compras.pdf"  # llamado clientes
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
    compras = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Compras", styles['Heading1'])
    compras.append(header)
    headings = ('No. Compra','Status','Total','Proveedor','Fecha Creacion')
    allcompras = [(c.num_compra, c.status, c.total, c.proveedor.nombre, c.fecha_creacion) for c in Compra.objects.all()]
    print (allcompras);

    t = Table([headings] + allcompras)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    compras.append(t)
    doc.build(compras)
    response.write(buff.getvalue())
    buff.close()
    return response

def reporte_contactos(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "contactos.pdf"  # llamado clientes
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
    contactos = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Contactos de Proveedores", styles['Heading1'])
    contactos.append(header)
    headings = ('Nombre','Telefono','Correo','Proveedor','Fecha Creacion')
    allcontactos = [(c.nombre,c.telefono,c.correo,c.proveedor.nombre,c.fecha_creacion) for c in ContactoProveedor.objects.all()]
    print (allcontactos);

    t = Table([headings] + allcontactos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    contactos.append(t)
    doc.build(contactos)
    response.write(buff.getvalue())
    buff.close()
    return response

def reporte_detalle_compra(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Detalle compra.pdf"  # llamado clientes
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
    detalles = []
    styles = getSampleStyleSheet()
    header = Paragraph("Detalle de compra", styles['Heading1'])
    detalles.append(header)
    headings = ('Numero de compra','Producto','Cantidad','Precio','Subtotal')
    alldetalles = [(d.compra,d.producto,d.cantidad,d.precio,d.subtotal) for d in DetalleCompra.objects.all()]
    print (alldetalles);

    t = Table([headings] + alldetalles)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (12, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    detalles.append(t)
    doc.build(detalles)
    response.write(buff.getvalue())
    buff.close()
    return response