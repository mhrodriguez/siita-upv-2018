# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Alumnos

# Register your models here.

class AdminAlumnos(admin.ModelAdmin):
    list_display = ["__unicode__", "matricula", "idplan", "idcarrera", "idpersona"]
    class Meta:
        model = Alumnos

admin.site.register(Alumnos, AdminAlumnos)
