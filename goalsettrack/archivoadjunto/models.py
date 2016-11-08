from django.db import models

from meta.models import MetaAbstracta


class ArchivoAdjunto(models.Model):
    """
    Una meta puede tener muchos archivos adjuntos,
    un archivo adjunto puede estar en una sola meta
    """
    titulo = models.CharField(max_length=80, default='TITULO ARCHIVO ADJUNTO')
    # los archivos se guardan en el subdirectorio archivos
    archivo = models.FileField(upload_to='archivos/')
    tiempo_creacion = models.DateTimeField(auto_now_add=True)
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)
