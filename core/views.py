from django.shortcuts import redirect, render
from .models import *
from functools import wraps

# Create your views here.
def medicos_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        try:
            username = request.session['username']
            try:
                medico = Medico.objects.get(correo = username)
                if medico.administrador != '1':
                    return function(request, user=medico)
                else:
                    return redirect('/subdirector/perfil')
            except Medico.DoesNotExist:
                request.session.flush()
                redirect('/login')
        except KeyError:
            return redirect('/login')
  return wrap

def logeado(request):
    try:
        username = request.session['username']
        return redirect('/inicio')
    except KeyError:
        return redirect('/login')

def inicio(request):
    try:
        username = request.session['username']
        return redirect('/inicio')
    except KeyError:
        return render(request,'core/inicio.html')

def login(request):
    ctx = {}
    ctx['error'] = False
    if request.method == 'GET':
        try:
            username = request.session['username']
            return redirect('/inicio')
        except KeyError:
            return render(request, 'core/login.html', ctx)
    elif request.method == 'POST':
        try:
            username = request.session['username']
            return redirect('/inicio')
        except KeyError:
            correo = request.POST['correo']
            password = request.POST['password']
            try:
                medico = Medico.objects.get(correo=correo, password=password)
                request.session['username'] = medico.correo
                return redirect('/inicio')
            except Medico.DoesNotExist:
                ctx['error'] = True
            return render(request, 'core/login.html', ctx)
def register(request):
    ctx = {}
    ctx['error'] = False
    if request.method == 'GET':
        try:
            username = request.session['username']
            return redirect('/inicio')
        except KeyError:
            return render(request, 'core/register.html', ctx)
    elif request.method == 'POST':
        try:
            username = request.session['username']
            return redirect('/inicio')
        except KeyError:
            correo = request.POST['correo']
            password = request.POST['password']
            try:
                medico = Medico.objects.get(correo=correo, password=password)
                request.session['username'] = medico.correo
                return redirect('/inicio')
            except Medico.DoesNotExist:
                ctx['error'] = True
            return render(request, 'core/register.html', ctx)

@medicos_only
def perfil(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'core/perfil.html', ctx)

@medicos_only
def programacion_cirugia(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'core/programacion_cirugia.html', ctx)

@medicos_only
def programacion_pabellon(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'core/programacion_pabellon.html', ctx)

@medicos_only
def reservar_pabellon(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'core/reservar_pabellon.html', ctx)

@medicos_only
def disponibilidad_pabellon(request, user=None):
    ctx = {}
    ctx['user'] = user
    return render(request, 'core/disponibilidad_pabellon.html', ctx)

@medicos_only
def disponibilidad_recursos(request, user=None):
    ctx = {}
    ctx['user'] = user
    ctx = {
        'recursos': {
            'Insumos disponibles': 15,
            'Unidades de apoyo clínico': 40,
            'Diagnóstico y terapeútico': 90,
            'Recursos humanos': 85,
            'Equipos quirúrgicos': 100,
        }, 
    }
    return render(request, 'core/disponibilidad_recursos.html', ctx)

@medicos_only
def reservar_recursos(request, user=None):
    ctx = {}
    ctx['user'] = user
    ctx = {
        'recursos': {
            'Insumos disponibles': 15,
            'Unidades de apoyo clínico': 40,
            'Diagnóstico y terapeútico': 90,
            'Recursos humanos': 85,
            'Equipos quirúrgicos': 100,
        }, 
    }
    return render(request, 'core/reservar_recursos.html', ctx)

def logout(request):
    request.session.flush()
    return redirect('/login')