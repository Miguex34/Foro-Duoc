from django.contrib import admin
from .models import *

# Register your models here.

admin.register(Escuela,Carrera,Estudiante
               ,Docente,Publicacion,Comentario)(admin.ModelAdmin)