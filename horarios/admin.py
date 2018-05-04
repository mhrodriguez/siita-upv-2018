# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Aulas, Materias, Carreras, Cuatrimestres, Grupos, Horarios

class AdminAulas(admin.ModelAdmin):
    list_display = ["id_aula", "edificio", "nombre","tipo"]
    search_fields = ["id_aula", "nombre"]
    class Meta:
        model = Aulas


admin.site.register(Aulas, AdminAulas)

class AdminMaterias(admin.ModelAdmin):
    list_display = ["id_materia", "nombre"]
    search_fields = ["id_materia", "nombre"]
    class Meta:
        model = Materias


admin.site.register(Materias, AdminMaterias)

class AdminCarreras(admin.ModelAdmin):
    list_display = ["id_carrera", "nombre"]
    search_fields = ["id_carrera", "nombre"]
    class Meta:
        model = Carreras


admin.site.register(Carreras, AdminCarreras)

class AdminCuatrimestres(admin.ModelAdmin):
    list_display = ["id_cuatrimestre", "nombre"]
    search_fields = ["id_cuatrimestre", "nombre"]
    class Meta:
        model = Cuatrimestres


admin.site.register(Cuatrimestres, AdminCuatrimestres)


class AdminGrupos(admin.ModelAdmin):
    list_display = ["id_grupo", "nombre", "id_materia", "id_maestro", "id_cuatrimestre"]
    search_fields = ["id_nombre", "nombre"]
    class Meta:
        model = Grupos


admin.site.register(Grupos, AdminGrupos)


class AdminHorarios(admin.ModelAdmin):
    list_display = ["id_horario", "id_aula", "id_grupo", "dia" ,"hora_entrada", "hora_salida"]
    search_fields = ["id_horario"]
    class Meta:
        model = Horarios


admin.site.register(Horarios, AdminHorarios)





