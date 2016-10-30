from django.shortcuts import render

# Create your views here.

def crear_comentario(request):
    return render(request, 'crear_comentario.html')

    