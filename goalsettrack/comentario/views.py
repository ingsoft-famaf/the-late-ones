"""
BASADO en https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/
content/homework_create_more_models/  para que andara deberia haber un
template meta_detalle que muestre la meta en detalle no entiendo bien lo de
pk, y tampoco como crear la relacion comentaio.meta = meta una vez que este
finalizado el modulo meta, creo que este modulo deberia con unas pocas
correcciones deberia poder funcionar.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from meta.models import Meta

from .forms import ComentarioFormulario
from .models import Comentario


@login_required
def crear_comentario(request, pk):
    """ Crea y agrega un comentario a una meta identificada por su id """
    # meta = get_object_or_404(Meta, pk=pk)
    meta = Meta.objects.get(pk=pk)
    # si ya se creo se guarda el comentario y se redirecciona el navegador a
    # la meta
    if request.method == "POST":
        form = ComentarioFormulario(request.POST)
        if form.is_valid():
        	  # Se crea el comentario con los datos del formulario
            comentario = form.save(commit=False)
            # se lo relaciona con la meta (foreing key y eso)
            comentario.meta = meta
            # se guarda el comentario en la base de datos
            comentario.save()
            #comentarios = Comentario.objects.filter(meta__pk=pk)
            return redirect('info_meta', pk=meta.id)
           # return render(request, 'detalle_comentario.html',
           #               {'comentario': comentario})
           # return render(request,'info_meta.html',
           #               {'meta': meta, 'comentarios': comentarios })
           # sino se crea un formulario vacio y se lo envia al template
           # crear_comentario, para que el usuario cree el comentario
           # cargando los datos.
    else:
        form = ComentarioFormulario(instance=meta)

    return render(request, 'crear_comentario.html', {'form': form})


@login_required
def lista_comentarios(request, pk):
    meta = Meta.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(meta__pk=pk)
    return render(request, 'lista_comentarios.html',
                  {'meta': meta, 'comentarios': comentarios})

@login_required
def eliminar_comentario(request, pk):
    comentario = Comentario.objects.get(pk=pk)
    meta = comentario.meta
    Comentario.objects.filter(pk=pk).delete()
    return redirect('info_meta', pk=meta.id)

@login_required
def editar_comentario(request, pk):
    comentario = Comentario.objects.get(pk=pk)
    meta = comentario.meta
    if request.method == "POST":
        form = ComentarioFormulario(request.POST, instance=comentario)
        if form.is_valid():
            # Se crea el comentario con los datos del formulario
            comentario = form.save(commit=False)
            # se lo relaciona con la meta
            comentario.meta = meta
            # se guarda el comentario en la base de datos
            comentario.save()
            return redirect('info_meta', pk=meta.id)
    else:
        form = ComentarioFormulario(instance=comentario)

    return render(request,'editar_comentario.html', { 'form': form })    


@login_required
def detalle_comentario(request, comentario_id):
    """
    En otra pagina el usuario elige ver un comentario en detalle, hace click
    en un boton, y eso postea el comentairo_id a esta funcion
    a partir de ese id, se busca y obtiene el comentario, y se lo muestra
    en el template detalle.html
    """
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    return render(request, 'detalle_comentario', {'comentario': comentario})



