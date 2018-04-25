# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Maestros (models.Model):
    id_maestro = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    num_empleado = models.IntegerField(validators=[MaxValueValidator(99999999)])
    nombres = models.CharField(max_length=45)
    ap_paterno = models.CharField(max_length=45)
    ap_materno = models.CharField(max_length=45)
    carrera = models.CharField(max_length=15)

    def __unicode__(self):    # Python 2
        return unicode(self.id_maestro)

    def __str__(self):        # Python 3
        return self.id_maestro