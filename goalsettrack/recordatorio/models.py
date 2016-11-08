from django.db import models

from meta.models import MetaAbstracta


class Recordatorio(models.Model):
    titulo = models.CharField(max_length=80, default='Título')
    mensaje = models.CharField(max_length=80, default='Mensaje')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField(blank=True)
    hora = models.TimeField(blank=True)
    repetir_cada = models.TimeField(blank=True)  # Tiempo de repeticion
    # Una meta tiene 0 o más recordatorios
    meta = models.ForeignKey(MetaAbstracta, on_delete=models.CASCADE)
