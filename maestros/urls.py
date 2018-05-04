from django.conf.urls import  url 
from django.views.generic import TemplateView

from . import views
urlpatterns = [
     #url(r'^mostrar', TemplateView.as_view(template_name='horario/mostrar.html'),name='horario/mostrar'),

   url(r'^$', views.horario),


  
    
]
