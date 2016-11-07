from django import forms

from .models import Meta, Submeta


class FormularioMeta(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de meta en la vista crear_meta
        model = Meta
        # el atributo de meta que no quiero que aprezca en la view
        exclude = ('user','fecha_comienzo', 'fecha_fin')
        fields = '__all__'


class FormularioSubMeta(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de submeta en la vista crear_submeta
        model = Submeta
        # los atributos de submeta que no quiero que aprezca en la view
        exclude = ('user','fecha_comienzo', 'fecha_fin', 'meta_origen')
        fields = '__all__'