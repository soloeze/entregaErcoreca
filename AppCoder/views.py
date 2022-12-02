from django.shortcuts import render
from .models import Tarea, Personas_del_equipo
from .forms import ContactoForm, TareaForm, Personas_del_equipoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    tareas = Tarea.objects.all()
    personas_del_equipo = Personas_del_equipo.objects.all()
    data = {
        'tareas': tareas,
        'personas_del_equipo': personas_del_equipo
    }
    return render(request,'AppCoder/home.html',data)

@csrf_exempt
def contacto(request):
    data = {
       'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario
    return render(request,'AppCoder/contacto.html', data)

def agregar_tarea(request):
    data = {
       'form': TareaForm()
    }
    if request.method == 'POST':
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Tarea guardada'
        else:
            data['form'] = formulario
    return render(request,'AppCoder/agregarTarea.html', data)

def agregar_personas_del_equipo(request):
    data = {
        'form': Personas_del_equipoForm()
    }
    if request.method == 'POST':
        formulario = Personas_del_equipoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Persona del equipo guardada'
        else:
            data['form'] = formulario
    
    return render(request,'AppCoder/agregarPersonasDelEquipo.html',data)

def buscarResultado(request):
    nombre_bus_views = request.GET['nombreBuscado']
    nombre_bus_res = Tarea.objects.filter(nombre=nombre_bus_views)
    return render(request,'AppCoder/resultadoDeBusqueda.html',{"nombre_view":nombre_bus_views, "nom_res":nombre_bus_res})

def buscarTarea(request):
    return render(request,'AppCoder/busqueda.html')
