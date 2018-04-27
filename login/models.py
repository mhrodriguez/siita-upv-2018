# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator

class UsuariosSiita (models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    usuario = models.CharField(max_length=10, null=False)
    contrasena =  models.CharField(max_length=20, null=False)


    def __unicode__(self):
        return unicode(self.id)  # Python 2

    def __str__(self):  # Python 3
        return self.id
