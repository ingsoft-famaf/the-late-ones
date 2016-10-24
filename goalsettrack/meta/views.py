from django.http import HttpResponse
from django.shortcuts import render


def crear_meta(request):
    return render(request, 'crear_meta.html')


def lista_de_metas(request):
    return render(request, 'lista_de_metas.html')
