from django.shortcuts import render
from .models import Autor, Editorial, Libro

# Create your views here.

def menu(request):
    return render(request, 'biblioteca/menu.html', {})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autores.html', {'autores': autores})

def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'biblioteca/editoriales.html', {'editoriales': editoriales})

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/libros.html', {'libros': libros})