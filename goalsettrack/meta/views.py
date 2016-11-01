# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from meta.models import Meta
from usuario.models import Usuario

from .forms import FormularioMeta


def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(user=usuario.id)
    return render(request, 'lista_de_metas.html', {'metas': metas, 'usuario': usuario})


def crear_meta(request):
    if request.method == "POST":
        form = FormularioMeta(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            usuario = Usuario.objects.get(usuario=request.user.id)
            meta.user_id = usuario.id
            meta.save()
            return redirect('lista_de_metas')
    else:
        form = FormularioMeta()
    return render(request, 'crear_meta.html', {'form': form})


def editar_meta(request, pk):
    meta = Meta.objects.get(pk=pk)
    if request.method == "POST":
        form = FormularioMeta(request.POST, instance=meta)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.save()
            return redirect('info_meta', pk=meta.pk)
    else:
        form = FormularioMeta(instance=meta)
    return render(request, 'editar_meta.html', {'form': form, 'meta': meta})


def info_meta(request, pk):
    meta = get_object_or_404(Meta, pk=pk)
    return render(request, 'info_meta.html', {'meta': meta})


def crear_submeta(request):
    return render(request, 'crear_submeta.html')
