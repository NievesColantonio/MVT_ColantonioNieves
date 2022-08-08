from operator import and_
from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares

# Create your views here.

def lista_familiares(request):
    familiares = Familiares.objects.all()
    lista_familiares_nombre = []
    lista_familiares_fecha_nacimiento = []

    for familiares in familiares:
        lista_familiares_nombre.append(familiares.nombre)
        lista_familiares_fecha_nacimiento.append(familiares.fecha_nacimiento)

    return HttpResponse(lista_familiares_nombre)
   
    


