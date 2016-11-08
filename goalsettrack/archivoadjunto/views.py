import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioArchAdj
from meta.models import *
from .models import *


@login_required
def subir_archivo(request, pk):
    meta = Meta.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormularioArchAdj(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.meta = meta
            archivo.save()
            message = "Archivo subido con exito!"
            return redirect('editar_meta', pk=meta.pk)
    else:
        form = FormularioArchAdj()
    return render(request, 'subir_archivo.html', {'form': form})

@login_required
def lista_archivos(request, pk):
    meta = Meta.objects.get(pk=pk)
    archivos = ArchivoAdjunto.objects.filter(meta__pk=pk)
    return render(request, 'lista_archivo_adj.html',
                  {'meta': meta, 'archivos': archivos})

@login_required
def eliminar_archivo(request, pk):
    archivo = ArchivoAdjunto.objects.get(pk=pk)
    meta = archivo.meta
    # se elimina archivo de server i.e directorio /archivos/ 
    os.remove(archivo.archivo.path)
    # se elimina archivo de la base de datos de django
    ArchivoAdjunto.objects.filter(pk=pk).delete()
    return redirect('info_meta', pk=meta.pk)



