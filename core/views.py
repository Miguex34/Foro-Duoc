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
                return function(request,**kwargs, user = estudiante)
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
def inicio(request,user):
    ctx = {}
    ctx['estudiante'] = user
    return render(request,'core/inicio.html', ctx)
    
@estudiantes_only
def forum(request,user):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        asunto = request.POST.get('asunto')
        descripcion = request.POST.get('descripcion')
        publicacion = Publicacion(titulo=titulo,asunto=asunto,descripcion=descripcion,id_estudiante=user)
        publicacion.save()
        return redirect('/forum')
    ctx = {}
    ctx['estudiante'] = user
    publicaciones = Publicacion.objects.all()
    if  'carrera' in request.GET:
        carrera = request.GET['carrera']
        filtro = Carrera.objects.get(nombre_carrera = Carrera.carreras_desc[carrera])
        autores = Estudiante.objects.all().filter(id_carrera = filtro)
        publicaciones = publicaciones.filter(id_estudiante__in = [autor.pk for autor in autores])
    ctx['publicaciones'] = publicaciones
    asuntos = Publicacion.OPCIONES_ASUNTO
    ctx['asuntos'] = asuntos
    return render(request,'core/forum.html', ctx)

@estudiantes_only
def publicacion(request,id,user):
    ctx = {}
    ctx['estudiante'] = user
    posteo = Publicacion.objects.get(pk=id)
    ctx['posteo'] = posteo
    if request.method == 'POST':
        texto = request.POST.get('comentario')
        comentario = Comentario(descripcion=texto,id_estudiante=user,id_publicacion=posteo)
        comentario.save()
        return redirect(f'/publicacion/{id}')
    comentarios=Comentario.objects.filter(id_publicacion=posteo).all()
    ctx['comentarios'] = comentarios
    return render(request,'core/publicacion.html', ctx)
        

def login(request):
    ctx = {}
    ctx['error'] = False
    if request.method == 'GET':
        try:
            correo = request.session['correo']
            return redirect('/inicio')
        except KeyError:
            return render(request, 'core/login.html', ctx)
    elif request.method == 'POST':
        
        if 'correo' in request.session:
            correo = request.session['correo']
        
            return redirect('/inicio')
        else:
            correo = request.POST.get('correo')
            contrasena = request.POST.get('contrasena')
            print(correo,contrasena)
            try:
                estudiante = Estudiante.objects.get(correo=correo, contrasena=contrasena)
                print('******++********************')
                request.session['correo'] = estudiante.correo
                print('******++*')
                return redirect('/inicio')
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