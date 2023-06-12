from django.urls import path
from .views import *

urlpatterns = [
    path('', logeado),
    path('inicio/', inicio),
    path('login/', login),
    #path('register/', register),
    path('forum/', forum),
    path('publicacion/<id>/', publicacion),
    path('logout/', logout),
]