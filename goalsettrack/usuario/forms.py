from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class FormularioUsuario(ModelForm):
  class Meta:
    model = Usuario
    exclude = ('usuario',)
    fields = '__all__'
