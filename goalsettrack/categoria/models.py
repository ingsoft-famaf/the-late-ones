from django.db import models

from usuario.models import Usuario


class Categoria(models.Model):
    """ Cada categoria es de un único usuario """
    titulo = models.CharField(max_length=80, default='Título')
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo