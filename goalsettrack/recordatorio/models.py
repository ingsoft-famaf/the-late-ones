from django.db import models
from meta.models import MetaAbstracta

class Recordatorio(models.Model):
    titulo = models.CharField(max_length=80, default='Título')
    mensaje = models.CharField(max_length=80, default='Mensaje')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Fecha de recordatorio
    fecha = models.DateField(blank=True)
    # Hora de recordatorio
    hora = models.TimeField(blank=True)
    # Tiempo de repeticion del recordatorio
    repetir_cada = models.TimeField(blank=True)
    # Una meta tiene 0 mas muchos recordatorios
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)
