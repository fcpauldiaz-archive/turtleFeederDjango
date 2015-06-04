#encoding:utf-8
#Universidad del Valle de Guatemala
#22/10/2014
#Pablo Diaz
#Archivo que controla las direcciones url dentro la pagina


from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()  #página de administrador

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turtleFeeder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','fedeer.views.inicio'), #direccion de inicio 
    #url(r'^/ssh','fedeer.views.ssh_connection'),#funcion que ejecuta una instruccion en la raspberry

    
    url(r'^$','fedeer.views.evento_feed'),
    url(r'^login','fedeer.views.login'),
    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#en este archivo la sintaxis es lo primero que se muestra despues de (r'^) es la direccion que va a tener en el servidor
#y lo que dice despues de views. es la funcion que llamará el programa cuando se llame a esa dirección
#la (r) significa que todo lo que está después es un raw string
#el signo (^) significa que allí empieza la dirección y el signo de dolar ($) significa que allí termina
