# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Maestros

# Register your models here.

class AdminMaestros(admin.ModelAdmin):
    list_display = ["__unicode__", "nombres", "ap_paterno", "ap_materno", "carrera"]
    class Meta:
        model = Maestros

admin.site.register(Maestros, AdminMaestros)

