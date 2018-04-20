# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Alumnos (models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    matricula = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    idplan = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    idcarrera = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    idpersona = models.IntegerField(validators=[MaxValueValidator(99999999999)])

    def __unicode__(self):
        return self.id  # Python 2


    def __str__(self):  # Python 3
        return self.id

