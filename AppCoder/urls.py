from django.urls import path
from .views import home,contacto,agregar_tarea,agregar_personas_del_equipo,buscarResultado,buscarTarea
#from AppCoder import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('agregartarea/',agregar_tarea, name='agregar_tarea'),
    path('agregarpersonasequipo/',agregar_personas_del_equipo, name='agregar_personas_del_equipo'),
    path('busquedaNombreTarea/', buscarTarea, name='busqueda'),
    path('buscar/', buscarResultado),
    
]