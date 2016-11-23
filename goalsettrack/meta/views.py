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


@login_required
def lista_de_metas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    metas = Meta.objects.filter(user=usuario.id)
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
def notificaciones(request):
    # se obtiene el usuario que esta logeado a quien se le enviara la notificacion
    usuario = Usuario.objects.get(usuario=request.user.id)
    # se obtiene las metas de dicho usuario
    metas = Meta.objects.filter(user=usuario.id)
    if request.method == 'GET':
        if request.is_ajax():
            # se obtiene la informacion a notificar, que es
            # las metas que han vencido, y los recordatorios que estan por expirar
            fecha_de_hoy = datetime.date.today()
            hora_actual = time.strftime("%H")
            hora_actual = hora_actual
            recordatorios_lista = []
            submetas_lista = []
            for meta in metas:
                # se obtienen los recordatorios de dicha meta, es decir, aquellos cuya
                # fecha y hora, coinciden con la fecha y hora actual 
                recordatorios = get_object_or_404(Recordatorio, pk=meta.id).values()
                recordatorios = recordatorios.filter(fecha=fecha_de_hoy).values()
                recordatorios = recordatorios.filter(hora=hora_actual).values()
                # se agregan los estos recordatorios a la lista de todos los recordatorios
                recordatorios_lista.append(recordatorios)
                # se agregan a la lista de submetas las submetas vencidas
                submetas = Submeta.objects.filter(meta_origen=meta.id)
                submetas = submetas.filter(fecha_vencimiento__lte=fecha_de_hoy)
                submetas_lista.append(submetas)
            recordatorio = 'Recordatorios: '
            for record in recordatorios_lista:
                recordatorio = recordatorio + record.titulo +':  '+ record.mensaje + '! '
            # se filtra las metas del usuario que se han vencido    
            metas = metas.filter(fecha_vencimiento__lte=fecha_de_hoy)
            vencimiento_metas = ' Metas vencidas: '
            for meta in metas:
                vencimiento_metas = vencimientos + '  ' + meta.titulo + ' '
                meta.estado = FALLIDA
                meta.fecha_fin = fecha_de_hoy
            # se filtra las submetas del usuario que se han vencido        
            vencimiento_submetas = ' Submetas vencidas: '
            for submeta in submetas_lista:
                vencimiento_submetas = vencimiento_submetas + ' ' + submeta.titulo + ' '
                submeta.estado = FALLIDA
                submeta.fecha_fin = fecha_de_hoy
            # se envia la notificacion
            data = {"vencimiento_submetas":vencimiento_submetas , "recordatorio" : recordatorio , "vencimiento_metas" : vencimiento_metas}
            return JsonResponse(data)
    return render(request, 'lista_de_metas.html',
                  {'metas': metas, 'usuario': usuario})

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
