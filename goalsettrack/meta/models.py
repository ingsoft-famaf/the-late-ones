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
    ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (EN_PROGRESO, 'En progreso'),
        (EN_PAUSA, 'En pausa'),
        (CUMPLIDA, 'Cumplida'),
        (ATRASADA, 'Atrasada'),
    )

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    PRIORIDADES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
        (E, 'E'),
        (F, 'F'),
    )

    abstract = True
    titulo = models.CharField(max_length=80, default='TITULO META')
    descripcion = models.CharField(max_length=1000, default='Descripcion.')
    estado = models.CharField(
        max_length=15, choices=ESTADOS, default=PENDIENTE)
    prioridad = models.CharField(max_length=15, choices=PRIORIDADES, default=A)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_comienzo = models.DateTimeField('comienzo', null=True, blank=True)
    fecha_fin = models.DateTimeField('fin', null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(
        'vencimiento', null=True, blank=True)


class Meta(MetaAbstracta):
    """
    Una relación muchos-a-uno. Requiere un argumento posicional: la clase a
    la que se relaciona el modelo.
    """

    # An object that has a many-to-one relationship
    # many 'Meta' to one 'Usuario'
    user = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Submeta(MetaAbstracta):
    """ Hereda de MetaAbstracta """

    # many 'Submetas' to one 'Meta'
    meta = models.ForeignKey('Meta', on_delete=models.CASCADE)
