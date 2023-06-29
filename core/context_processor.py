from .models import Carrera

def obtener_carreras(request):
    carrera = Carrera.objects.all()
    carreras = [i.get_nombre_carrera_display() for i in carrera]
    return {'carreras':carreras}