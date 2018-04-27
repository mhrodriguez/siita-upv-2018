from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator

class Alumnos (models.Model):
    id_alumno = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    nombres = models.CharField(max_length=45)
    ap_paterno = models.CharField(max_length = 45)
    ap_materno = models.CharField(max_length = 45)
    matricula = models.IntegerField(validators=[MaxValueValidator(9999999999)])


    def __unicode__(self):
        return unicode(self.id_alumno)  # Python 2


    def __str__(self):  # Python 3
        return self.id_alumno
