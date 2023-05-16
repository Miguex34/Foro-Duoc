from django.shortcuts import render, redirect
from core.models import *
from functools import wraps

# Create your views here.

def subdirector_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            username = request.session['username']
            try:
                medico = Medico.objects.get(correo = username)
                if medico.administrador in '1':
                    return function(request ,user=medico)
                else:
                    return redirect('/perfil')
            except Medico.DoesNotExist:
                request.session.flush()
                redirect('/login')
        except KeyError:
            return redirect('/login')
    return wrap

def inicio(request):
    return redirect('subdirector/perfil')

@subdirector_only
def perfil(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'subdirector/perfil.html', ctx)

@subdirector_only
def disponibilizar_pabellon(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'subdirector/disponibilizar_pabellon.html', ctx)

@subdirector_only
def informe(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'subdirector/informe.html', ctx)

@subdirector_only
def disponibilizar_recursos(request, user=None):
    ctx = {
        'recursos': {
            'Insumos disponibles': 15,
            'Unidades de apoyo clínico': 40,
            'Diagnóstico y terapeútico': 90,
            'Recursos humanos': 85,
            'Equipos quirúrgicos': 100,
        }, 
    }
    return render(request, 'subdirector/disponibilizar_recursos.html', ctx)