""" Tablas de la base de datos sobre Metas """

from django.db import models
from usuario.models import Usuario


class MetaAbstracta(models.Model):
    """ Atributos y métodos comunes a Meta y Submeta """

    PENDIENTE = 'Pendiente'
    EN_PROGRESO = 'En progreso'
    EN_PAUSA = 'En pausa'
    CUMPLIDA = 'Cumplida'
    ATRASADA = 'Atrasada'
    PRIO_A = 'A'
    PRIO_B = 'B'
    PRIO_C = 'C'
    PRIO_D = 'D'
    PRIO_E = 'E'
    PRIO_F = 'F'
    ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (EN_PROGRESO, 'En progreso'),
        (EN_PAUSA, 'En pausa'),
        (CUMPLIDA, 'Cumplida'),
        (ATRASADA, 'Atrasada'),
    )
    PRIORIDADES = (
        (PRIO_A, 'A'),
        (PRIO_B, 'B'),
        (PRIO_C, 'C'),
        (PRIO_D, 'D'),
        (PRIO_E, 'E'),
        (PRIO_F, 'F'),
    )
    abstract = True
    titulo = models.CharField(max_length=80, default='Título')
    descripcion = models.CharField(max_length=1000, default='Descripción')
    estado = models.CharField(choices=ESTADOS, default=PENDIENTE)
    prioridad = models.CharField(choices=PRIORIDADES, default=PRIO_A)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_comienzo = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)


class Meta(MetaAbstracta):
    """ Hereda de MetaAbstracta """

    # cada meta es de 1 usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Submeta(MetaAbstracta):
    """ Hereda de MetaAbstracta """

    # cada submeta es de 1 meta
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
