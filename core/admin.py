from django.contrib import admin
from .models import *

# Register your models here.

admin.register(Atencion,BitacoraCirugia,Cargo,
                Cirugia,Ciudad,DetalleUnidad,
                DisponibilidadPabellon,Evaluacion,Medico,
                Modulo,Pabellon,Paciente,ProgramacionCirugia,
                Recurso,Region,ReservaPabellon,ReservaRecurso,
                Unidad,)(admin.ModelAdmin)