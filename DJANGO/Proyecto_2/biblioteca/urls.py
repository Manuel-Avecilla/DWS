from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('autores/', views.autores, name='autores'),
    path('editoriales/', views.editoriales, name='editoriales'),
    path('libros/', views.libros, name='libros'),
]