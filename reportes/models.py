# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from persona.models import Persona


class Parentesco(models.Model):
    nombre = models.CharField(max_length=30)
    parientes = models.ManyToManyField(
        Persona,
        through='Relaciones',
        through_fields=('parentesco', 'persona'),
    )

    def __unicode__(self):
        return self.nombre


class Relaciones(models.Model):
    parentesco = models.ForeignKey(Parentesco)
    persona = models.ForeignKey(Persona)
    persona2 = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='persona_relacionada',
    )

class Parejas(models.Model):
    persona = models.ForeignKey(Persona)
    persona2 = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='pareja',
    )
    estado = models.BooleanField()