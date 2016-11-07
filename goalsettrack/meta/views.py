# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from meta.models import Meta
from usuario.models import *

from .forms import FormularioMeta
from notify.signals import notify
import datetime


@login_required
def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    actual_user = get_object_or_404(User, username=request.user)
    metas = Meta.objects.filter(user=usuario.id)
    #current_time = datetime.datetime.now().time()
    #if current_time.isoformat() == '18:08:00.000000':
    notify.send(usuario, recipient=actual_user, actor=usuario,verb='Tenes cero metas')
    return render(request, 'lista_de_metas.html', {'metas': metas, 'usuario': usuario})


@login_required
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


@login_required
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


@login_required
def info_meta(request, pk):
    meta = get_object_or_404(Meta, pk=pk)
    return render(request, 'info_meta.html', {'meta': meta})


# @login_required
# def crear_submeta(request):
#     return render(request, 'crear_submeta.html')
