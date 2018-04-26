from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator

class Alumnos (models.Model):
    matricula = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    nombres = models.CharField(max_length=45)
    ap_paterno = models.CharField(max_length = 45)
    ap_materno = models.CharField(max_length = 45)


    def __unicode__(self):   # Python 2
        return unicode(self.matricula)


    def __str__(self):  # Python 3
        return self.matricula
