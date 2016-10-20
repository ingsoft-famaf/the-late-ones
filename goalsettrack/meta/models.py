""" Tablas de la base de datos sobre Metas """

from django.db import models


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

    titulo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=1000)
    estado = models.CharField(max_length=15, choices=ESTADOS)
    prioridad = models.CharField(max_length=15, choices=PRIORIDADES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_comienzo = models.DateTimeField('comienzo')
    fecha_fin = models.DateTimeField('fin')
    fecha_vencimiento = models.DateTimeField('vencimiento')

    def modificar(self):
        """ Modificar los atributos """
        pass


class Meta(MetaAbstracta):
    """ Hereda de MetaAbstracta """

    pass
