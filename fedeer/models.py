#encoding:utf-8
#Universidad del Valle de Guatemala
#22/10/2014
#Pablo Diaz
#Archivo donde se maneja la informacion de la base de datos
#models.py

from django.db import models
from django.db.models.signals import post_save #se importa la funcion para manejar el usuario
from django.contrib.auth.models import User#módulo estándar de django para manejar los usuarios que están ingresados 
from django.core.exceptions import ValidationError#módulo estándar para regresar un error al ingresar un dato en las entradas. 
from django.core.validators import MaxValueValidator, MinValueValidator#validacion estandar para los digitos del nit
from django.db.models.base import ModelBase 
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode #sirve para tener una variedad amplia de caracteres 

import copy
import datetime

#funcion para validar el nombre
def validar_nombre(value):
    num = value.isnumeric()
    alpha = value.isalpha()
    #esta validacion da problema porque no deja ingresar espacios en el nombre
    if alpha == False:#si el nombre no es alfabetico da error
        raise ValidationError('Ingrese un nombre válido')
    
    if num == True:#da error si el usuario ingresa numeros, pero no controla la mezcla de numeros y letras
        raise ValidationError('El nombre no pueden ser números')


# Create your models here.

class EventoFeed(models.Model):
    fecha=models.DateField(auto_now_add=True,auto_now=False)#se guarda la fecha cuando se guarda 
    hora=models.TimeField(auto_now_add=True,auto_now=False)#se guarda la hora de creacion
    tiempo_comida=models.IntegerField(null=True,blank=True,default=15)#el usuario ingresa la cantidad de comida

    def __unicode__(self):
        return smart_unicode(self.fecha,self.hora,self.tiempo_comida)

class Contacto(models.Model):
    nombre=models.CharField(verbose_name="Nombre completo", max_length=30,validators = [validar_nombre])
    correo = models.EmailField(verbose_name='Tu correo electronico')
    usuario=models.ForeignKey(User,blank=True,null=True)#usuario 
    mensaje = models.TextField(verbose_name="mensaje")

    def __unicode__(self):
       
        return smart_unicode(self.nombre, self.correo, self.usuario)#el return en general sirve para mostar el valor definido aqui en el panel admin


        
