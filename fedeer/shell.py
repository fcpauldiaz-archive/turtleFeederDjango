#encoding:utf-8
#Díaz Reyes & Asociados
#Views.py
#Pablo Díaz
#19/10/2014
#Archivo que ejecuta una instruccion en la terminal de la raspberry
import subprocess

def ejecutar(k,v):
	if k =="tiempo_comida":
		subprocess.call("pi4j Servo "+v,shell=True)
 
