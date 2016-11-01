# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormularioMeta
from django.contrib.auth.decorators import login_required
from usuario.models import *
from meta.models import *

def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario = request.user.id)
    metas = Meta.objects.filter(user = usuario.id)
    return render(request, 'lista_de_metas.html', {'metas' : metas})

def crear_meta(request):
    if request.method == "POST":
        form = FormularioMeta(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            usuario = Usuario.objects.get(usuario = request.user.id)
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
    return render(request, 'editar_meta.html', {'form': form})

def info_meta(request, pk):
    meta = get_object_or_404(Meta, pk=pk)
    return render(request, 'info_meta.html', {'meta': meta})

def crear_submeta(request):
    return render(request, 'crear_submeta.html')
