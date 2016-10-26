# from django.http import HttpResponse
from django.shortcuts import render

def lista_de_metas(request):
    return render(request, 'lista_de_metas.html')

def crear_meta(request):
    return render(request, 'crear_meta.html')

def crear_submeta(request):
    return render(request, 'crear_submeta.html')
