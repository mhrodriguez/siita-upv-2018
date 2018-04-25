# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegForm

# Create your views here.

def cita(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("")
    context = {
        "form": form,
    }
    return render(request, 'cita.html', context)