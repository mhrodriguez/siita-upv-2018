from django.shortcuts import render
from django.views.generic import TemplateView
from alumnos.models import Alumnos
from horarios.models import Aulas, Materias,Grupos,Horarios,Cuatrimestres,Carreras
from maestros.models import Maestros
from django.http import HttpResponse


class BuscarView(TemplateView):
    template_name = 'horarios/encontrado.html'
    
    

def horario_list(request):
    alumno = Alumnos.objets.all() 



         