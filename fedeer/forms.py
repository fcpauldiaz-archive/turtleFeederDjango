#encoding:utf-8
#Díaz Reyes & Asociados
#forms.py
#8/03/2014
#pablo diaz 
#en este archivo los formularios para que el validar los datos ingresados por el usuario

from django.forms import ModelForm #modulo estandar de django para crear formularios
from django import forms#los formularios permiten que el usuario ingrese los datos en los modelos creados
from fedeer.models import EventoFeed,Contacto#se importa el modelo hecho
from django.contrib.auth.models import User #libreria del tipo usuario


#clase que representa el formulario para hacer contacto con el administrador de la página
class ContactoForm(ModelForm):
        class Meta:
                model = Contacto
        
class RegistrationForm(forms.ModelForm):
        class Meta:
                model=EventoFeed