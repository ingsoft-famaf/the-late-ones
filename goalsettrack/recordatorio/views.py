from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from usuario.models import Usuario
from meta.models import Meta
from recordatorio.models import Recordatorio
from recordatorio.forms import RecordatorioFormulario

@login_required
def crear_recordatorio(request, pk):
    meta_pk = Meta.objects.get(pk=pk)
    if request.method == "POST":
        form = RecordatorioFormulario(request.POST)
        if form.is_valid():
            recordatorio = Recordatorio()
            recordatorio.titulo = form.cleaned_data['titulo']
            recordatorio.mensaje_email = form.cleaned_data['mensaje']
            recordatorio.fecha = form.cleaned_data['fecha']
            recordatorio.hora = form.cleaned_data['hora']
            recordatorio.repetir_cada = form.cleaned_data['tiempo_repeticion']
            recordatorio.meta = meta_pk
            recordatorio.save()
            return redirect('lista_recordatorio_meta', pk=meta_pk.pk)
    else:
        form = RecordatorioFormulario()
    return render(request, 'crear_recordatorio.html', {'form': form})


@login_required
def lista_recordatorio_meta(request, pk):
	meta = Meta.objects.get(pk=pk)
	recordatorios = Recordatorio.objects.filter(meta=meta).values()
	return render(request, 'lista_recordatorio_meta.html', { 'recordatorios': recordatorios, 'meta': meta })


@login_required
def eliminar_recordatorio(request, pk):
	recordatorio = get_object_or_404(Recordatorio, pk=pk)
	meta = recordatorio.meta
	Recordatorio.objects.filter(pk=pk).delete()
	return redirect('lista_recordatorio_meta', pk=meta.pk)


@login_required
def info_recordatorio(request, pk):
	recordatorio = get_object_or_404(Recordatorio, pk=pk)
	return render(request, 'info_recordatorio.html', { 'recordatorio': recordatorio })


@login_required
def editar_recordatorio(request, pk):
    pass
