from django.db import models
from meta.models import MetaAbstracta
import datetime

class Comentario(models.Model):
    """
    Clase que moldea los comentarios hecho por el usuario en las metas o submetas.
    Cada comentario es de una única meta / submeta ie cada comentario es único
    """
    texto = models.CharField(max_length=1000, default='Comentario.')
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now) # sino funciona probar models.DateTimeField(default=timezone.now)
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)

