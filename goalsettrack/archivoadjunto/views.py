from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from meta.models import Meta

from .forms import FormularioArchAdj
from .models import ArchivoAdjunto


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
            return redirect('lista_de_metas')
    else:
        form = FormularioArchAdj()
    return render(request, 'subir_archivo.html', {'form': form})


@login_required
def lista_archivos(request, pk):
    meta = Meta.objects.get(pk=pk)
    archivos = ArchivoAdjunto.objects.filter(meta__pk=pk)
    return render(request, 'lista_archivo_adj.html',
                  {'meta': meta, 'archivos': archivos})
