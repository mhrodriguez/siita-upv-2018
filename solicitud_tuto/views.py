# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegForm

# Create your views here.

def cita(request):
    form = RegForm()
    context = {
        "form": form,
    }
    return render(request, 'cita.html', context)