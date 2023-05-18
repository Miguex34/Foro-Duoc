from django.urls import path
from .views import *

urlpatterns = [
    path('', logeado),
    path('inicio/', inicio),
    path('login/', login),
    path('register/', register),
    path('perfil/', perfil),
    path('logout/', logout),
    path('programacion/cirugia/', programacion_cirugia),
    path('programacion/pabellon/', programacion_pabellon),
    path('programacion/pabellon/reservar/', reservar_pabellon),
    path('programacion/recursos/reservar/', reservar_recursos),
    path('programacion/pabellon/disponibilidad/', disponibilidad_pabellon),
    path('programacion/recursos/disponibilidad/', disponibilidad_recursos),
]