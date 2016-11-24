# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from comentario.models import Comentario
from meta.models import Meta, Submeta, FALLIDA, CUMPLIDA
from usuario.models import Usuario
from recordatorio.models import *
import time
import datetime
from .forms import FormularioMeta, FormularioSubMeta
from meta.helper import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


#API KEY para enviar mail  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

MAIL_APP = "goalsettrack@sendgrid.com"


@login_required
def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(user=usuario.id)
   # send_mail("GOAL SET TRACK IGNA2", "HELLO WORLD SPAM JAA2",
    #    "goalsettrack@sendgrid.com", ["ignamadevollen@gmail.com"])
    # se asigna el progreso de cada meta i.e porcentaje de submetas cumplidas de sus submetas
    for meta in metas:
        submetas = Submeta.objects.filter(meta_origen=meta.id)
        submetas_total = submetas.count()
        submetas_completadas = submetas.filter(estado=CUMPLIDA).count()
        if submetas_total != 0:
            # porcentaje
            meta.progreso = (submetas_completadas/submetas_total) * 100
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
            meta.fecha_creacion = datetime.date.today()
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
            submeta.fecha_creacion = datetime.date.today()
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

### VIEW DE NOTIFICACIONES

@login_required
def envio_mails(request):
    # se obtiene el usuario que esta logeado a quien se le enviara la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    if request.method == 'GET':
        #se manda mail a los usuarios no conectados y que tienen mail
        usuarios = Usuario.objects.all().exclude(mail='email')
        usuarios = usuarios.exclude(mail='')
        usuarios = usuarios.exclude(usuario=request.user.id)
        asunto = "GOAL SET TRACK : The-late-ones Notificacion"
        enviar_mail_a(usuarios,asunto,MAIL_APP)
    return redirect('lista_de_metas')


@login_required
def recordatorio_instantaneo(request):
    # se obtiene el usuario que esta logeado a quien se le enviara la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    
    if request.method == 'GET':
        # se obtiene la informacion que se le enviara al usuario en la notificacion:
        # metas vencidas, submetas vencidas, y recordatorios
        if request.is_ajax():
            vencimiento_recordatorios = ''
            vencimiento_recordatorios = recordatorios_vencidos(usuario)
            if vencimiento_recordatorios != '' and vencimiento_recordatorios != 'Recordatorios vencidos: ':
                data = { 'vencimiento_recordatorios' : vencimiento_recordatorios }
                return JsonResponse(data)
    return redirect('lista_de_metas')

@login_required
def notificaciones(request):
    # se obtiene el usuario que esta logeado a quien se le enviara la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    
    if request.method == 'GET':
        if request.is_ajax():
            vencimiento_metas = ''
            vencimiento_metas = metas_vencidas(usuario)
            vencimiento_submetas = ''
            vencimiento_submetas = submetas_vencidas(usuario)
            vencimiento_recordatorios = ''
            vencimiento_recordatorios = recordatorios_vencidos(usuario)
            if vencimiento_recordatorios != '' or vencimiento_metas != '' or vencimiento_submetas != '':
                data = {'vencimiento_metas' : vencimiento_metas, 'vencimiento_submetas' : vencimiento_submetas, 'vencimiento_recordatorios' : vencimiento_recordatorios }
                return JsonResponse(data)
    return redirect('lista_de_metas')

@login_required
def ver_notificaciones(request):
    # se obtiene el usuario que esta logeado, quien obtendra la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    vencimiento_metas = ''
    vencimiento_metas = metas_vencidas(usuario)
    vencimiento_submetas = ''
    vencimiento_submetas = submetas_vencidas(usuario)
    vencimiento_recordatorios = ''
    vencimiento_recordatorios = recordatorios_vencidos(usuario)
    return render(request, 'ver_notificaciones.html',{'vencimiento_metas' : vencimiento_metas, 'vencimiento_submetas' : vencimiento_submetas, 'vencimiento_recordatorios' : vencimiento_recordatorios })

    


#### VIEW DE PROGRESO MENSUAL

@login_required
def progreso_mensual(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(user=usuario.id)
    primer_dia_mes_actual = datetime.datetime.now()
    # seteo la fecha al primer dia del mes actual
    primer_dia_mes_actual.replace(day=1)
    # metas creadas a partir del dia uno de este mes, o en el dia 1 de este mes
    # ie, las metas creadas este mes
    metas_creadas = metas.filter(fecha_creacion__lte=primer_dia_mes_actual)
    # las metas cumplidas de las creadas el ultimo mes, es responsabilidad del usuario
    # de asignar una meta como cumplida
    metas_cumplidas = metas_creadas.filter(estado=CUMPLIDA)
    # las metas fallidas de las creadas el ultimo mes, el usuario puede asignar este estado
    # manualmente, o tambien se hace automaticamente, cuando una mete vence
    metas_fallidas = metas_creadas.filter(estado=FALLIDA)
    return render(request, 'progreso_mensual.html', {'metas_creadas': metas_creadas, 'metas_cumplidas': metas_cumplidas,'metas_fallidas': metas_fallidas})


