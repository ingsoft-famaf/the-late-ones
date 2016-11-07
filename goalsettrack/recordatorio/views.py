from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from recordatorio.forms import RecordatorioFormulario
from recordatorio.models import *
from meta.models import Meta
from usuario.models import Usuario


"""
BASADO en https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/
content/homework_create_more_models/ 
"""


# Create your views here.

@login_required
def crear_recordatorio(request, pk):
    # meta = get_object_or_404(Meta, pk=pk)
    meta = Meta.objects.get(pk=pk)
    # si ya se creo se guarda el recordatorio y se redirecciona el navegador a la
    # meta
    if request.method == "POST":
        form = RecordatorioFormulario(request.POST)
        if form.is_valid():
        	  # se crea el recordatorio con los datos del formulario
            recordatorio = form.save(commit=False)
            # se lo relaciona con la meta
            recordatorio.meta = meta
            # se guarda el recordatorio en la base de datos
            recordatorio.save()
            return redirect('lista_recordatorio_meta',pk=meta.pk)
           # return render(request, 'detalle_recordatorio.html',
           #               {'recordatorio': recordatorio})
           # return render(request,'info_meta.html',
           #               {'meta': meta, 'recordatorios': recordatorios })
           # sino se crea un formulario vacio y se lo envia al template
           #  crear_recordatorio, para que el usuario cree el recordatorio
           # cargando los datos
    else:
        form = RecordatorioFormulario()
    return render(request, 'crear_recordatorio.html', {'form': form})


@login_required
def lista_recordatorio_meta(request, pk):
	meta = Meta.objects.get(pk=pk)
	# A veces la anterior forma de consulta devolvia error para recordatorio, por lo que se la hace del sig modo
	recordatorios = Recordatorio.objects.filter(meta=meta).values()
	return render(request, 'lista_recordatorio_meta.html', { 'recordatorios': recordatorios, 'meta': meta })

@login_required
def eliminar_recordatorio(request, pk):
	recordatorio = get_object_or_404(Recordatorio, pk=pk)
	meta = recordatorio.meta
	Recordatorio.objects.filter(pk=pk).delete()
	return redirect('lista_recordatorio_meta',pk=meta.pk)


@login_required
def info_recordatorio(request, pk):
	recordatorio = get_object_or_404(Recordatorio, pk=pk)
	return render(request, 'info_recordatorio.html', { 'recordatorio': recordatorio })


@login_required
def editar_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    meta = recordatorio.meta
    if request.method == "POST":
        form = RecordatorioFormulario(request.POST, instance=recordatorio)
        if form.is_valid():
            recordatorio = form.save(commit=False)
            recordatorio.meta = meta
            recordatorio.save()
            return redirect('info_recordatorio', pk=recordatorio.pk)
    else:
        form = RecordatorioFormulario(instance=recordatorio)
    return render(request, 'editar_recordatorio.html', {'form': form, 'recordatorio': recordatorio})	