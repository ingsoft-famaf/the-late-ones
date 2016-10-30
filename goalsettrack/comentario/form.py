from django import forms
from .models import Comentario

class ComentarioFormulario(forms.ModelForm):
	"""
	Clase para manejar Formularios utilizados por el browser para
	crear comentarios
    """

    class Meta:
        model = Comentario
        fields = '__all__' # todos los atributos de la clase Comentario

        