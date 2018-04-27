# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegForm
from .models import Solicitudes_citas

# Create your views here.

def cita(request):
    form = RegForm(request.POST or None)
        
    context = {
        "form": form,
    }

    if form.is_valid():
        form_data = form.cleaned_data
        tip = form_data.get("tipo")
        fec = form_data.get("fecha")
        lug = form_data.get("lugar")
        com = form_data.get("comentarios")
        db_register = Solicitudes_citas(tipo=tip, fecha=fec, lugar=lug, comentarios=com)
        db_register.save()

    return render(request, 'cita.html', context)