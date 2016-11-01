from django import forms
from categoria.models import Categoria

class CategoriaFormulario(forms.ModelForm):

    class Meta:
        model = Categoria
        # el atributo de categoria que no quiero que aprezca en la view
        exclude = ('user',)
        fields = '__all__' # todos los atributos de la clase Categoria

        