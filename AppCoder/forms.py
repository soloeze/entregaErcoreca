from django import forms
from .models import Contacto, Tarea, Personas_del_equipo

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

        widgets = {
            'fecha_de_creacion':forms.SelectDateWidget()
        }

class Personas_del_equipoForm(forms.ModelForm):
    class Meta:
        model = Personas_del_equipo
        fields = '__all__'
        
