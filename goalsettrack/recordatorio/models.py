from django.db import models
from datetime import datetime

# Create your models here.

class Recordatorio(models.Model):
    titulo = models.CharField(max_length=80, default='TITULO RECORDATORIO')
    fecha =models.DateTimeField('recordatorio', null=True, blank=True)
    hora = models.TimeField()
    repetir_cada = models.IntegerField(default=3)
    mensaje = models.CharField(max_length=80, default='MENSAJE RECORDATORIO')
