from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import messages
from . import forms
from . import models


# Create your views here.
def main(request):
    """
    Vista principal
    """
    return render(request, 'planeacion/index.html')



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
    return render(request, 'planeacion/mostrar.html', {'planeacion': planeacion})




