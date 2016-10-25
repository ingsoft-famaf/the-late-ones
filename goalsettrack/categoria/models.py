from django.db import models
from usuario.models import Usuario

# Create your models here.

class Categoria(models.Model):
    """ Clase categoria para clasificar o agrupar las distintas metas """
    # como no se asigna clave primaria, django crea un atributo 'id' como clave primaria
    categoria = models.CharField(max_length=80, default='TITULO CATEGORIA')
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)

