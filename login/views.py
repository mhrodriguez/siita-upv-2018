from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from .forms import LogForm
from .models import UsuariosSiita

# from django.http import HttpRequest
# Create your views here.

def inicio(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        usuario_log = data.get("usuario")
        contra_log = data.get("contrasena")
        # print(usuario_log)
        # print(contra_log)
        acceso = authenticate(username=usuario_log, password=contra_log)
        if acceso is not None:
            login(request,acceso)
            return HttpResponse("Bienvenido")
            # return HttpRequest.path("siita/templates/inicio.html")
        else:
            return HttpResponse("Usuario / Contrasena incorrectos")
    else:
        form = LogForm()


    context ={
        "el_form": form,
    }
    # return HttpRequest.path("/siita/templates/login.html")
    return render(request, "login.html", context)
