# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from alumnos.models import Alumnos
from maestros.models import Maestros

# Create your models here.

class Solicitudes_citas (models.Model):
    id_cita = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    id_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 15)
    fecha = models.DateField()
    lugar = models.CharField(max_length = 45)
    comentarios = models.CharField(max_length = 225)
    

    def __unicode__(self):   # Python 2
        return unicode(self.id_cita)


    def __str__(self):  # Python 3
        return self.id_cita