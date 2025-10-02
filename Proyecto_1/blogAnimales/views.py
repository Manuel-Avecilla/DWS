from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.

def menu (request) :
    return render (request, 'blogAnimales/menu.html', {})

def animales (request) :
    animales = Animal.objects.all()
    return render (request, 'blogAnimales/animales.html', {'animales': animales})

def protectoras (request) :
    protectoras = Protectora.objects.all()
    return render (request, 'blogAnimales/protectoras.html', {'protectoras': protectoras})

def colaboradores (request) :
    colaboradores = Colaborador.objects.all()
    return render (request, 'blogAnimales/colaboradores.html', {'colaboradores': colaboradores})