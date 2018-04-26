# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Solicitudes_citas

# Register your models here.

class AdminSolicitudes_citas(admin.ModelAdmin):
    list_display = ["__unicode__", "matricula", "num_empleado", "tipo", "fecha", "lugar", "comentarios"]
    class Meta:
        model = Solicitudes_citas

admin.site.register(Solicitudes_citas, AdminSolicitudes_citas)


