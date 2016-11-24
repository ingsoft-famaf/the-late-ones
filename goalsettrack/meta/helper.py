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
from django.utils import timezone
from .forms import FormularioMeta, FormularioSubMeta
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
# FUNCIONES AUXILIARES PARA OBTENER LA INFORMACION QUE SE ENVIA EN LA NOTIFICACION



def enviar_mail_a(usuarios, asunto, emisor):
    for usuario in usuarios:
        metas = Meta.objects.filter(user=usuario.id).exclude(estado=FALLIDA)
        mensaje = 'Metas a vencer: '
        for meta in metas:
            mensaje = mensaje + ' ' + meta.titulo
        receptor = usuario.mail
        if receptor == '':
            print("excluir")
        print(usuario.nombre)
        print(asunto)
        print(mensaje)
        print(emisor)
        print(receptor) 
        send_mail(asunto, mensaje, emisor, [receptor])  


def metas_vencidas(usuario):
    # se obtiene las metas de dicho usuario
    metas = Meta.objects.filter(user=usuario.id)
    # se obtiene la informacion a notificar, que es
    # las metas que han vencido, y los recordatorios que estan por expirar
    fecha_de_hoy = timezone.now()
    # se filtra las metas del usuario que se han vencido    
    metas = metas.filter(fecha_vencimiento__lte=fecha_de_hoy)
    vencimiento_metas = ' Metas vencidas: '
    for meta in metas:
        vencimiento_metas = vencimientos_metas + '  ' + meta.titulo + ' '
        meta.estado = FALLIDA
        meta.fecha_fin = fecha_de_hoy
    
    return vencimiento_metas

def submetas_vencidas(usuario):
    # se obtiene las submetas de dicho usuario
    submetas = Submeta.objects.filter(meta_origen__user=usuario.id)
    # se obtiene la informacion a notificar, que es
    # las submetas que han vencido, y los recordatorios que estan por expirar
    fecha_de_hoy = timezone.now()
    # se filtra las submetas del usuario que se han vencido    
    submetas = submetas.filter(fecha_vencimiento__lte=fecha_de_hoy)
    vencimiento_submetas = ' Submetas vencidas: '
    for submeta in submetas:
        vencimiento_submetas = vencimiento_submetas + '  ' + submeta.titulo + ' '
        submeta.estado = FALLIDA
        submeta.fecha_fin = fecha_de_hoy
    
    return vencimiento_submetas

def recordatorios_vencidos_de_meta(meta, fecha_de_hoy, hora_actual):
    recordatorios = Recordatorio.objects.filter(meta=meta)
    # se obtiene los recordatorios del usuario que han vencido
    recordatorios = recordatorios.filter(fecha=fecha_de_hoy)
    recordatorios = recordatorios.filter(hora=hora_actual)
    recordatorios_vencidos = ''
    for recordatorio in recordatorios:
        recordatorios_vencidos = recordatorios_vencidos + ' ' + recordatorio.titulo
    return recordatorios_vencidos 


def recordatorios_vencidos(usuario):
    fecha_de_hoy = timezone.now()
    # la hora tiene este formato HH:MM[:ss[.uuuuuu]]
    now = datetime.datetime.now()
    hora_actual = str(now).split()[1]
    metas = Meta.objects.filter(user=usuario.id)
    vencimiento_recordatorios = ' Recordatorios vencidos: '
    for meta in metas:
        vencimiento_recordatorios = vencimiento_recordatorios + '  ' + recordatorios_vencidos_de_meta(meta, fecha_de_hoy, hora_actual)
    return vencimiento_recordatorios    



