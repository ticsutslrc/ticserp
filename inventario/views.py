# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from . import forms
from . import models

# Create your views here.
def main(request):
    """
    Vista principal de modulo de inventarios
    """
    return render(request, 'inventario/index.html')