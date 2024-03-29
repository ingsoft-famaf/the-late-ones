import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from meta.models import Meta
from recordatorio.forms import RecordatorioFormulario
from recordatorio.models import Recordatorio


@login_required
def crear_recordatorio(request, pk):
    meta = Meta.objects.get(pk=pk)
    if request.method == "POST":
        form = RecordatorioFormulario(request.POST)
        if form.is_valid():
            recordatorio = form.save(commit=False)
            recordatorio.meta = meta
            recordatorio.save()
            return redirect('lista_recordatorio_meta', pk=meta.pk)
    else:
        form = RecordatorioFormulario(instance=meta)
    return render(request, 'crear_recordatorio.html', {'form': form})


@login_required
def lista_recordatorio_meta(request, pk):
    meta = Meta.objects.get(pk=pk)
    recordatorios = Recordatorio.objects.filter(meta=meta).values()
    return render(request, 'lista_recordatorio_meta.html',
                  {'recordatorios': recordatorios, 'meta': meta})


@login_required
def eliminar_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    meta = recordatorio.meta
    Recordatorio.objects.filter(pk=pk).delete()
    return redirect('lista_recordatorio_meta', pk=meta.pk)


@login_required
def info_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    return render(request, 'info_recordatorio.html',
                  {'recordatorio': recordatorio})


@login_required
def editar_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    if request.method == "POST":
        form = RecordatorioFormulario(request.POST, instance=recordatorio)
        if form.is_valid():
            recordatorio = form.save(commit=False)
            recordatorio.save()
            return render(request, 'info_recordatorio.html',
                          {'recordatorio': recordatorio})
    else:
        form = RecordatorioFormulario(instance=recordatorio)
    return render(request, 'editar_recordatorio.html', {'form': form})


@login_required
def eliminar_recordatorios_viejos(request, pk):
    # basado en https://tutorial.djangogirls.org/es/django_orm/
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    meta = recordatorio.meta
    fecha_de_hoy = datetime.date.today()
    # se entiende por viejos aquellos recordatorio de aquellas metas que
    # tienen como estado cumplida o cuya fecha de vencimiento es menor que
    # la fecha de hoy
    # Se eliminan los recordatorios de las metas cumplidas
    Recordatorio.objects.filter(meta__estado='cumplida').delete()
    # se eliminan los recordatorios cuya fecha de vencimiento expiro
    Recordatorio.objects.filter(
        meta__fecha_vencimiento__lte=fecha_de_hoy).delete()

    return redirect('lista_recordatorio_meta', pk=meta.pk)


@login_required
def adelantar_recordatorios_meta(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    meta = recordatorio.meta
    Recordatorio.objects.filter(meta=meta).update(hora='10:00:00')
    return redirect('lista_recordatorio_meta', pk=meta.pk)


@login_required
def atrasar_recordatorios_meta(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    meta = recordatorio.meta
    Recordatorio.objects.filter(meta=meta).update(hora='10:00:00')
    return redirect('lista_recordatorio_meta', pk=meta.pk)
