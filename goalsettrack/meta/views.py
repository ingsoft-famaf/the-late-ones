# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from comentario.models import Comentario
from meta.models import Meta, Submeta
from usuario.models import Usuario
from recordatorio.models import *
import time
import datetime
from .forms import FormularioMeta, FormularioSubMeta


@login_required
def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(user=usuario.id)
    return render(request, 'lista_de_metas.html',
                  {'metas': metas, 'usuario': usuario})

@login_required
def notificaciones(request):
    # se obtiene el usuario que esta logeado a quien se le enviara la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    # se obtiene las metas de dicho usuario
    metas = Meta.objects.filter(user=usuario.id)
    if request.method == 'GET':
        if request.is_ajax():
            # se obtiene la informacion a notificar, que es
            # las metas y submetas que han vencido, y los recordatorios que estan por expirar
            fecha_de_hoy = datetime.date.today()
            hora_actual = time.strftime("%H")
            hora_actual = hora_actual
            recordatorios_lista = []
            for meta in metas:
                # se obtienen los recordatorios de dicha meta, es decir, aquellos cuya
                # fecha y hora, coinciden con la fecha y hora actual 
                recordatorios = get_object_or_404(Recordatorio, pk=meta.id).values()
                recordatorios = recordatorios.filter(fecha=fecha_de_hoy).values()
                recordatorios = recordatorios.filter(hora=hora_actual).values()
                # se agregan los estos recordatorios a la lista de todos los recordatorios
                recordatorios_lista.append(recordatorios)

            recordatorio = 'Recordatorios: '
            for record in recordatorios_lista:
                recordatorio = recordatorio + record.titulo +':  '+ record.mensaje + '! '
            email = 'igna_made@gmail.com'
            data = {"email":email , "recordatorio" : recordatorio}
            return JsonResponse(data)
    return render(request, 'lista_de_metas.html',
                  {'metas': metas, 'usuario': usuario})

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
def info_meta(request, pk):
    meta = get_object_or_404(Meta, pk=pk)
    return render(request, 'info_meta.html', {'meta': meta})


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
def eliminar_meta(request, pk):
    meta = Meta.objects.get(pk=pk)
    # se eliminan todos las submetas de la meta
    Submeta.objects.filter(meta_origen=meta.id).delete()
    # se eliminan todos los comentarios de la meta
    Comentario.objects.filter(meta=meta.id).delete()
    meta.delete()
    return redirect('lista_de_metas')


@login_required
def filtrar_meta(request):
    if request.method == "POST":
        s_titulo = request.POST.get('titulo', 'Vv')
        # usuario = Usuario.objects.get(usuario=request.user.id)
        # metas = Meta.objects.filter(titulo=s_titulo and user=usuario.id)
        metas = Meta.objects.filter(titulo=s_titulo)
        return render(request, 'filtrar_meta.html', {'metas': metas})
    return redirect('lista_de_metas')

# Views de Submeta ############################


@login_required
def lista_de_submetas(request, pk):
    meta = Meta.objects.get(pk=pk)
    submetas = Submeta.objects.filter(meta_origen=meta.id)
    return render(request, 'lista_de_submetas.html',
                  {'submetas': submetas, 'meta': meta})


@login_required
def crear_submeta(request, pk):
    if request.method == "POST":
        form = FormularioSubMeta(request.POST)
        if form.is_valid():
            submeta = form.save(commit=False)
            meta = Meta.objects.get(pk=pk)
            submeta.meta_origen = meta
            submeta.save()
            return redirect('lista_de_submetas', pk=meta.pk)
    else:
        form = FormularioSubMeta()
    return render(request, 'crear_submeta.html', {'form': form})


@login_required
def info_submeta(request, pk):
    submeta = get_object_or_404(Submeta, pk=pk)
    return render(request, 'info_submeta.html', {'submeta': submeta})


@login_required
def editar_submeta(request, pk):
    submeta = Submeta.objects.get(pk=pk)
    if request.method == "POST":
        form = FormularioSubMeta(request.POST, instance=submeta)
        if form.is_valid():
            submeta = form.save(commit=False)
            submeta.save()
            return redirect('info_submeta', pk=submeta.pk)
    else:
        form = FormularioSubMeta(instance=submeta)
    return render(request, 'editar_submeta.html',
                  {'form': form, 'submeta': submeta})


@login_required
def eliminar_submeta(request, pk):
    Submeta.objects.get(pk=pk).delete()
    return redirect('lista_de_metas')
