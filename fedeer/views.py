#encoding:utf-8
#Universidad del Valle de Guatemala
#Views.py
#Pablo Díaz
#23/10/2014
#Archivo que controla todas las funciones lógicas que utiliza el programa



from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect#funciones de para manipular las acciones de http
from django.shortcuts import render_to_response, get_object_or_404#para dar el problema clasico 404
from django.template import RequestContext #sirve para que funcione las stylesheets css y demas archivos en /static
from django.core.mail import EmailMessage#para ingresar correo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm#función predeterminada de django para crear usuario y validarlo
from django.contrib.auth import login, authenticate, logout#para iniciar y terminar sesion
from django.contrib.auth.decorators import login_required# libreria que sirve para determinar en que página se neceista una sesion previa para acceder a ella
from django.http import Http404 #sirve para dar el error 404 cuando está en un servidor y no se encuentra la página que se está buscando.
from django.views.decorators.csrf import  csrf_protect , csrf_exempt#cross site request forgery protection (esto es mas util cuando un proyecto esta funcionando en la web)
from django.db import IntegrityError #sirve para agarrar la excepción que produce
from django.contrib.auth.models import Group# sirve para añadir a los usuarios al grupo especificado
from django.contrib import messages #sirve para mostrar un mensaje condicional al usuario
import subprocess #ejecutar comando de ssh
from shell import * #archivo personalizado para ejecutar instrucciones en la raspberry
from fedeer.models import EventoFeed
from fedeer.forms import RegistrationForm
# Create your views here.

def inicio(request):
	evento = EventoFeed.objects.all()
	return render_to_response('index.html',{'evento':evento},context_instance=RequestContext(request))
@csrf_exempt
def evento_feed(request):
	k=""
	v=""
	for k, v in request.POST.iteritems():
		print k, v


	evento = EventoFeed.objects.all()
	if request.method=='POST':
		formulario = RegistrationForm(request.POST)
		
		if formulario.is_valid():
			formulario.save()
			ejecutar(k,v)           #se manda a llamar al programa que ejecuta un comando en la raspberry, se manda de parametro la key y el valor
			return HttpResponseRedirect('http://domesticfeeder.servehttp.com:8020')
	else:
		formulario=RegistrationForm()

	return render_to_response('index.html',{'formulario':formulario,'evento':evento},context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html',context_instance=RequestContext(request))

