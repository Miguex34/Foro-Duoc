from django.shortcuts import redirect, render
from .models import *
from functools import wraps

# Create your views here.
def estudiantes_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            correo = request.session['correo']
            try:
                estudiante = Estudiante.objects.get(correo = correo)
                return redirect('/forum')
            except Estudiante.DoesNotExist:
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
    
@estudiantes_only
def inicio(request):
    return render(request,'core/inicio.html')
    
@estudiantes_only
def forum(request):
    return render(request,'core/forum.html')

def login(request):
    ctx = {}
    ctx['error'] = False
    if request.method == 'GET':
        try:
            correo = request.session['correo']
            return redirect('/forum')
        except KeyError:
            return render(request, 'core/login.html', ctx)
    elif request.method == 'POST':
        try:
            correo = request.session['correo'][0]
            return redirect('/forum')
        except KeyError:
            correo = request.POST['correo']
            contrasena = request.POST['contrasena']
            try:
                estudiante = Estudiante.objects.get(correo=correo, contrasena=contrasena)
                request.session['correo'] = estudiante.correo
                return redirect('/forum')
            except Estudiante.DoesNotExist:
                ctx['error'] = True
            return render(request, 'core/login.html', ctx)

'''def register(request):
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
            return render(request, 'core/register.html', ctx)'''
        
        
def logout(request):
    request.session.flush()
    return redirect('/login')