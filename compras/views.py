# -*- coding: utf-8 -*-
"""
Compras vistas
Aqui se van a poner todas las vistas de compras
"""
from django.shortcuts import render


def main(request):
    """
    Vista principal de compras
    """
    return render(request, 'compras/index.html')
