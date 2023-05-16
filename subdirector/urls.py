from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('perfil/', perfil),
    path('disponibilizar/pabellon/', disponibilizar_pabellon),
    path('informe/', informe),
    path('disponibilizar/recursos/', disponibilizar_recursos)
]