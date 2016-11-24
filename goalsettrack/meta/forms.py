from django import forms

from .models import Meta, Submeta, Categoria


class FormularioMeta(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categoria.objects.all())

    class Meta:
        # modelo usado para el formulario de meta en la vista crear_meta
        model = Meta
        # el atributo de meta que no quiero que aprezca en la view
        exclude = ('user', 'fecha_creacion', 'fecha_fin', 'progreso')
        fields = '__all__'


class FormularioSubMeta(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de submeta en la vista crear_submeta
        model = Submeta
        # los atributos de submeta que no quiero que aprezca en la view
        exclude = ('user', 'fecha_creacion', 'fecha_fin', 'meta_origen', 'progreso')
        fields = '__all__'
