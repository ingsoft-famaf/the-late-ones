from django import forms

from recordatorio.models import Recordatorio


class RecordatorioFormulario(forms.ModelForm):

    class Meta:
        model = Recordatorio
        # el atributo de categoria que no quiero que aprezca en la view
        exclude = ('meta',)
        fields = '__all__' # todos los atributos de la clase Categoria
