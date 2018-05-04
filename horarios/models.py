# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from maestros.models import Maestros

from django.core.validators import MaxValueValidator


# Create your models here.
class Aulas (models.Model):
     id_aula = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])     
     edificio = models.CharField(max_length = 10)
     nombre = models.CharField(max_length = 10, null=True)

     tipo = models.CharField(max_length = 15) 


     def __unicode__(self):   # Python 2
        return unicode(self.id_aula)


     def __str__(self):  # Python 3
        return self.id_aula

class Materias (models.Model):
     id_materia = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])            
     nombre =  models.CharField(max_length = 25)


class Carreras (models.Model):
     id_carrera = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])            
     nombre =  models.CharField(max_length = 25)

     def __unicode__(self):   # Python 2
        return unicode(self.id_carrera)


     def __str__(self):  # Python 3
        return self.id_carrera

class Cuatrimestres (models.Model):
     id_cuatrimestre = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])            
     nombre =  models.CharField(max_length = 25) 

     def __unicode__(self):   # Python 2
        return unicode(self.id_cuatrimestre)


     def __str__(self):  # Python 3
        return self.id_cuatrimestre




class Grupos (models.Model):
     id_grupo = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
     nombre = models.CharField(max_length = 10, null=True)
     id_materia = models.ForeignKey(Materias, on_delete=models.CASCADE)
     id_maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE)
     id_cuatrimestre = models.ForeignKey(Cuatrimestres, on_delete=models.CASCADE)

     def __unicode__(self):   # Python 2
        return unicode(self.id_grupo)


     def __str__(self):  # Python 3
        return self.id_grupo

class Horarios (models.Model):
     id_horario = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
     id_aula = models.ForeignKey(Aulas, on_delete=models.CASCADE)
     id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
     dia =  models.CharField(max_length = 10)
     hora_entrada = models.TimeField(['%I:%H %p'], blank=True, null=True)
     hora_salida = models.TimeField(['%I:%H %p'], blank=True, null=True)

     def __unicode__(self):   # Python 2
        return unicode(self.id_horario)


     def __str__(self):  # Python 3
        return self.id_horario   


        



