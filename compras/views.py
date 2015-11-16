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
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from . import forms
from . import models
from .models import Proveedor


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




def CompraConsultar(request):
    """
    Vista para consulta de proveedores
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
            form.save()
            #
            messages.add_message(request, messages.INFO, 'Compra agregada con exito')
            return HttpResponseRedirect(reverse('compras:compra_consultar'))
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
    ContactoProveedor = get_object_or_404(models.Compra, pk=pk)
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

def generar_pdf(request):
    print ("Genero el PDF");
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "proveedores.pdf"  # llamado clientes
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