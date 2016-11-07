from django.db import models

from categoria.models import Categoria
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
    descripcion = models.CharField(max_length=1000, default='Descripción.')
    estado = models.CharField(
        max_length=11, choices=ESTADOS, default=PENDIENTE)
    prioridad = models.CharField(
        max_length=1, choices=PRIORIDADES, default=PRIO_A)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_comienzo = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)


class Meta(MetaAbstracta):
    """ Cada meta tiene 0 o 1 categoría """
    user = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True, null=True)


class Submeta(MetaAbstracta):
    """ Cada submeta es de una única meta """

    meta_origen = models.ForeignKey(
        Meta, on_delete=models.CASCADE, blank=True, null=True)
