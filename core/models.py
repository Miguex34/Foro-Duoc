# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models
import datetime

class Escuela(models.Model):
    NOMBRES_ESCUELAS = [
        ('escinf','Escuela de Informática y Telecomunicaciones'),
        ('escomun','Escuela de Comunicación'),
        ('escadmin','Escuela de Administración y Negocios'),
    ]
    id_escuela = models.BigAutoField(primary_key=True)
    nombre_escuela = models.CharField(max_length=50,choices = NOMBRES_ESCUELAS)

class Carrera(models.Model):
    NOMBRES_CARRERAS = [
        ('ingin','Ingeniería en Informática'),
        ('ingred','Ingeniería en Conectividad y Redes'),
        ('publ','Publicidad'),
        ('digt','Animación Digital'),
        ('ingmark','Ingeniería en Marketing Digital'),
        ('audi','Auditoría'),
    ]
    id_carrera = models.BigAutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=50,choices = NOMBRES_CARRERAS)
    id_escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)

class Estudiante(models.Model):
    id_estudiante = models.BigAutoField(primary_key=True)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=500)
    id_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido_p

class Docente(models.Model):
    id_docente = models.BigAutoField(primary_key=True)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=500)
    id_escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Docentes'

class Publicacion(models.Model):
    id_publicacion = models.BigAutoField(primary_key=True)
    asunto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    id_estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)

class Comentario(models.Model):
    id_comentario = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    id_estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    id_publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
