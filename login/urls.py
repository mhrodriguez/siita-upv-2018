from django.conf.urls import url, include
from login.views import inicio
from . import views

urlpatterns = [
    url(r'^$', inicio),
]
