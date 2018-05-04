from django.shortcuts import render
from django.views.generic import TemplateView
from alumnos.models import Alumnos
from django.http import HttpResponse
from.forms import in_mat



def horario(request):
    titulo="Maticula"

    form = in_mat(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        print form_data.get("matricula")
    context ={
        "tem_titulo": titulo,
        "el_form": form,
    }
    return render(request, 'maestros/buscar.html',context)



