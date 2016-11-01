from usuario.models import Categoria
from django.forms import ModelForm


class CategoriaFormulario(ModelForm):
	"""
	Clase que representa un formulario para ser utilizado por el browser
	y las views de categoria para crear, eliminar y asginar categorias
	"""

    class Meta:
        model = Categoria
        fields = '__all__'
