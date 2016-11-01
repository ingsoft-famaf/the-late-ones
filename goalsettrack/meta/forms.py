from django import forms

from .models import Meta


class FormularioMeta(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de meta en la vista crear_meta
        model = Meta
        # el atributo de meta que no quiero que aprezca en la view
        exclude = ('user',)
        fields = '__all__'
