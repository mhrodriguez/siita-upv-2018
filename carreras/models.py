from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator

class Carreras (models.Model):
    id = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    nombre = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nombre  # Python 2


    def __str__(self):  # Python 3
        return self.nombre