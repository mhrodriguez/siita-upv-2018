from __future__ import unicode_literals

from django.contrib import admin

from .models import UsuariosSiita

class AdminUsuariosSiita(admin.ModelAdmin):
    list_display = ["id", "usuario", "contrasena"]
    search_fields = ["id", "usuario"]
    class Meta:
        model = UsuariosSiita


admin.site.register(UsuariosSiita, AdminUsuariosSiita)
