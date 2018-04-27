# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Solicitudes_citas (models.Model):
    id_cita = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    id_alumno = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    id_maestro = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    tipo = models.CharField(max_length = 15)
    fecha = models.DateField()
    lugar = models.CharField(max_length = 45)
    comentarios = models.CharField(max_length = 225)


    def __unicode__(self):
        return unicode(self.id_cita)


    def __str__(self):  # Python 3
        return self.id_cita
