from django import forms
from .models import ArchivoAdjunto


class FormularioArchAdj(forms.ModelForm):

    class Meta:
        model = ArchivoAdjunto
        exclude = ('meta',)
        fields = '__all__'
