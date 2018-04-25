# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Alumnos (models.Model):
    id_alumno = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    nombres = models.CharField(max_length=45)
    ap_paterno = models.CharField(max_length = 45)
    ap_materno = models.CharField(max_length = 45)
    matricula = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    

    def __unicode__(self):   # Python 2
        return unicode(self.id_alumno)


    def __str__(self):  # Python 3
        return self.id_alumno

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

class Solicitudes_citas (models.Model):
    id_cita = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    id_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE)
    nombres = models.ForeignKey(Maestros, on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 15)
    fecha = models.DateField()
    lugar = models.CharField(max_length = 45)
    comentarios = models.CharField(max_length = 225)
    

    def __unicode__(self):   # Python 2
        return unicode(self.id_cita)


    def __str__(self):  # Python 3
        return self.id_cita