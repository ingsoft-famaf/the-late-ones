from django.db import models

# Create your models here.
class Comentario(models.Model):
	texto = models.CharField(max_length=1000, default='Comentario')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
