from django.shortcuts import get_object_or_404, render
from .models import Categoria, Meta, Usuario
from .forms import CategoriaFormulario
# Create your views here.


# BASADO en https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/homework_create_more_models/
# para que andara deberia haber un template meta_detalle que muestre la meta en detalle
# no entiendo bien lo de pk, y tampoco como crear la relacion categoria.meta = meta
# una vez que este finalizado el modulo meta, creo que este modulo deberia con unas pocas correcciones
# deberia poder funcionar

# crea y agrega un categoria a una meta identificada por su id
def crear_categoria(request, meta_id):
    meta = get_object_or_404(Meta, pk=meta_id)
    # si ya se creo se guarda el categoria y se redirecciona el navegador a la meta
    if request.method == "POST":
        form = categoriaFormulario(request.POST)
        if form.is_valid():
        	# se crea el categoria con los datos del formulario
            categoria = form.save(commit=False)
            # se lo relaciona con la meta (foreing key y eso)
            # probablemente esto no anda, se deberia hacer una consulta sql y usar lo de las filiminas
            categoria.meta = meta
            # habria que relacionarlo con el usuario tambien.. no se como desde aca
            # se guarda el categoria en la base de datos
            categoria.save()
            return redirect('meta_detalle', pk=meta.id)
    # sino se crea un formulario vacio y se lo envia al template crear_categoria, para que 
    # el usuario cree el categoria cargando los datos        
    else:
        form = CategoriaFormulario()
    return render(request, 'categoria/crear_categoria.html', {'form': form})    

# en otra pagina el usuario elige ver un categoria en detalle, hace click en un boton,
# y eso postea el categoria_id a esta funcion
# a partir de ese id, se busca y obtiene el categoria, y se lo muestra
# en el template detalle.html
def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(categoria, pk=categoria_id)
    return render(request, 'categoria/detalle_categoria.html', {'categoria': categoria})

# se elimina un categoria
# desde la view de meta usuario hace ckick en eliminar categoria, que pasa
# el id de tal categoria a esta funcion, esta funcion obtiene de la base de datos
# tal categoria a partir del id pasado, obtiene la meta en la que esta a traves de
# la foreign key, elimina el categoria de la meta y redirecciona al usuario para 
# el detalle de las metas
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(categoria, pk=categoria_id)
    # probablemente esto no anda, se deberia hacer una consulta sql y usar lo de las filiminas
    meta = categoria.meta
    del categoria 
    return redirect('meta_detalle', pk=meta.id)