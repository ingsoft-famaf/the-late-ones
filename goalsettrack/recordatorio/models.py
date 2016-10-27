from django.db import models


class Recordatorio(models.Model):
    """ Una meta puede tener muchos recordatorios, un comentario puede estar en una sola meta"""
    titulo = models.CharField(max_length=80, default='Título')
    fecha = models.DateTimeField()
    hora = models.TimeField(null=True, blank=True)
    repetir_cada = models.IntegerField(default=0)
    mensaje = models.CharField(max_length=1000, default='Mensaje')
    user = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)
