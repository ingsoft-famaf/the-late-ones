from django.db import models

# Create your models here.
class Comentario(models.Model):
    """ Una meta puede tener muchos comentarios, un comentario puede estar en una sola meta"""
	texto = models.CharField(max_length=1000, default='Comentario')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)
