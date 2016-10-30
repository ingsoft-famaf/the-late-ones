from django.db import models
from meta.models import MetaAbstracta
import datetime

class Comentario(models.Model):
    """ cada comentarios es de una única meta / submeta """
    texto = models.CharField(max_length=1000, default='Comentario.')
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now)
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)

