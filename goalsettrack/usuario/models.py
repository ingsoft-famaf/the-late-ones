from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save

class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True)
    nombre = models.CharField(max_length=30, blank=True)
    mail = models.EmailField(max_length=70, blank=True)

    def __string__(self):
        return str(self.nombre)

@receiver(post_save, sender=User)
def crear_perfil_para_usuario_nuevo(sender, created, instance, **kwargs):

    if created:
        perfil = Usuario(usuario=instance)
        perfil.save()

