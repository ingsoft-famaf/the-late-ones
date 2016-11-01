from django.shortcuts import get_object_or_404, render, redirect
from categoria.models import *
from categoria.forms import CategoriaFormulario
from meta.models import *
# Create your views here.


# BASADO en https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/homework_create_more_models/
# para que andara deberia haber un template meta_detalle que muestre la meta en detalle
# no entiendo bien lo de pk, y tampoco como crear la relacion comentaio.meta = meta
# una vez que este finalizado el modulo meta, creo que este modulo deberia con unas pocas correcciones
# deberia poder funcionar

# crea una categoria 
def crear_categoria(request):
    #meta = get_object_or_404(Meta, pk=pk)
    usuario = Usuario.objects.get(usuario = request.user.id)
    # si ya se creo se guarda el categoria y se redirecciona el navegador a la meta
    if request.method == "POST":
        form = CategoriaFormulario(request.POST)
        if form.is_valid():
        	# se crea el categoria con los datos del formulario
            categoria = form.save(commit=False)
            # se lo relaciona con el usuario (foreing key y eso)
            categoria.user = usuario
            # se guarda el categoria en la base de datos
            categoria.save()
            return redirect('lista_de_metas')
           # return render(request, 'detalle_categoria.html', {'categoria': categoria})
           # return render(request,'info_meta.html', {'meta': meta, 'categorias': categorias })
    # sino se crea un formulario vacio y se lo envia al template crear_categoria, para que 
    # el usuario cree el categoria cargando los datos        
    else:
        form = CategoriaFormulario()
    return render(request, 'crear_categoria.html', { 'form': form }) 

# se muestra las categorias del usuario
def lista_categorias(request):
    # se obtiene el usuario 
    usuario = Usuario.objects.get(usuario = request.user.id)
    # se obtienen todas las categorias a partir del id del usuario
    categorias = Categoria.objects.filter(user = usuario.id)
    return render(request,'lista_categorias.html', { 'categorias': categorias })

def eliminar_categoria(request, pk):
    # se obtiene el usuario 
    usuario = Usuario.objects.get(usuario = request.user.id)
    # se obtiene la categoria a eliminar
    Categoria.objects.filter(pk=pk).delete()
    # se obtienen todas las categorias a partir del id del usuario
    categorias = Categoria.objects.filter(user = usuario.id)
    return render(request,'lista_categorias.html', { 'categorias': categorias })