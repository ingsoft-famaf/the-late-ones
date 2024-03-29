from django import forms

from .models import Comentario


class ComentarioFormulario(forms.ModelForm):

    class Meta:
        model = Comentario
        # el atributo de comentario que no quiero que aprezca en la view
        exclude = ('meta',)
        # todos los atributos de la clase Comentario
        fields = '__all__'
