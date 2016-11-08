from django.forms import ModelForm

from usuario.models import Usuario


class FormularioUsuario(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('usuario',)
        fields = '__all__'
