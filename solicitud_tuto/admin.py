# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Solicitudes_citas
from .models import Alumnos

# Register your models here.

class AdminSolicitudes_citas(admin.ModelAdmin):
    list_display = ["__unicode__", "id_alumno", "id_maestro", "tipo", "fecha", "lugar", "comentarios"]
    class Meta:
        model = Solicitudes_citas

admin.site.register(Solicitudes_citas, AdminSolicitudes_citas)

class AdminAlumnos(admin.ModelAdmin):
    list_display = ["__unicode__", "nombres", "ap_paterno", "ap_materno", "matricula"]
    class Meta:
        model = Alumnos

admin.site.register(Alumnos, AdminAlumnos)

