from django.shortcuts import get_object_or_404, render, redirect
from .models import Comentario
from .forms import ComentarioFormulario
from meta.models import *
# Create your views here.


# BASADO en https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/homework_create_more_models/
# para que andara deberia haber un template meta_detalle que muestre la meta en detalle
# no entiendo bien lo de pk, y tampoco como crear la relacion comentaio.meta = meta
# una vez que este finalizado el modulo meta, creo que este modulo deberia con unas pocas correcciones
# deberia poder funcionar

# crea y agrega un comentario a una meta identificada por su id
def crear_comentario(request, pk):
    #meta = get_object_or_404(Meta, pk=pk)
    meta = Meta.objects.get(pk=pk)
    # si ya se creo se guarda el comentario y se redirecciona el navegador a la meta
    if request.method == "POST":
        form = ComentarioFormulario(request.POST)
        if form.is_valid():
        	# se crea el comentario con los datos del formulario
            comentario = form.save(commit=False)
            # se lo relaciona con la meta (foreing key y eso)
            comentario.meta = meta
            # se guarda el comentario en la base de datos
            comentario.save()
            #comentarios = Comentario.objects.filter(meta__pk=pk)
            return redirect('info_meta', pk=meta.id)
           # return render(request, 'detalle_comentario.html', {'comentario': comentario})
           # return render(request,'info_meta.html', {'meta': meta, 'comentarios': comentarios })
    # sino se crea un formulario vacio y se lo envia al template crear_comentario, para que 
    # el usuario cree el comentario cargando los datos        
    else:
        form = ComentarioFormulario(instance=meta)
    return render(request, 'crear_comentario.html', {'form': form}) 

def lista_comentarios(request, pk):
    meta = Meta.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(meta__pk=pk)
    return render(request,'lista_comentarios.html', {'meta': meta, 'comentarios': comentarios })

# en otra pagina el usuario elige ver un comentario en detalle, hace click en un boton,
# y eso postea el comentairo_id a esta funcion
# a partir de ese id, se busca y obtiene el comentario, y se lo muestra
# en el template detalle.html
def detalle_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    return render(request, 'detalle_comentario', {'comentario': comentario})

# se elimina un comentario
# desde la view de meta usuario hace ckick en eliminar comentario, que pasa
# el id de tal comentairo a esta funcion, esta funcion obtiene de la base de datos
# tal comentario a partir del id pasado, obtiene la meta en la que esta a traves de
# la foreign key, elimina el comentario de la meta y redirecciona al usuario para 
# el detalle de las metas
def eliminar_comentario(request, pk):
    comentario = Comentario.objects.get(pk=pk)
    meta = comentario.meta
    del comentario 
    return redirect('info_meta', pk=meta.id)