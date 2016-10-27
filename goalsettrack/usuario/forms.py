from usuario.models import Usuario
from django.contrib.auth.models import User
from django.forms import ModelForm


class FormularioUsuario(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('usuario',)
        fields = '__all__'
