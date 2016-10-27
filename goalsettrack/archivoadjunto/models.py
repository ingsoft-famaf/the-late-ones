from django.db import models

# Create your models here.
class ArchivoAdjunto(models.Model):
        """ Una meta puede tener muchos archivos adjuntos, un archivo adjunto puede estar en una sola meta"""
		titulo = models.CharField(max_length=80, default='TITULO ARCHIVO ADJUNTO')
		tamanio = models.IntegerField(default=100)
		archivo = models.FileField(upload_to='archivos/') # los archivos se guardan en el subdirectorio archivos
		tiempo_creacion = models.DateTimeField(auto_now_add=True)
        meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)