# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models

class Atencion(models.Model):
    id_atencion = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    id_medico = models.ForeignKey('Medico', models.CASCADE, db_column='id_medico')
    id_paciente = models.ForeignKey('Paciente', models.CASCADE, db_column='id_paciente')
    id_interconsulta = models.OneToOneField('self', models.CASCADE, db_column='id_interconsulta', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'atencion'
        verbose_name_plural = 'Atenciones'


class BitacoraCirugia(models.Model):
    id_bitacora_cirugia = models.BigAutoField(primary_key=True)
    detalle = models.CharField(max_length=3000)
    fecha = models.DateField()
    hora = models.DateTimeField()
    id_cirugia = models.ForeignKey('Cirugia', models.CASCADE, db_column='id_cirugia')

    class Meta:
        managed = True
        db_table = 'bitacora_cirugia'
        verbose_name_plural = 'Bitacoras de cirugia'


class Cargo(models.Model):
    id_cargo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descripcion


class Cirugia(models.Model):
    id_cirugia = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    id_reserva_cirugia = models.OneToOneField('ProgramacionCirugia', models.CASCADE, db_column='id_reserva_cirugia')

    class Meta:
        managed = True
        db_table = 'cirugia'
        verbose_name_plural = 'Cirugias'


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    id_region = models.ForeignKey('Region', models.CASCADE, db_column='id_region')

    class Meta:
        managed = True
        db_table = 'ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.descripcion


class DetalleUnidad(models.Model):
    id_detalle_unidad = models.BigAutoField(primary_key=True)
    id_unidad = models.ForeignKey('Unidad', models.CASCADE, db_column='id_unidad')
    id_medico = models.ForeignKey('Medico', models.CASCADE, db_column='id_medico')

    class Meta:
        managed = True
        db_table = 'detalle_unidad'
        verbose_name_plural = 'Detalle unidades'


class DisponibilidadPabellon(models.Model):
    id_disponibilidad_pabellon = models.BigAutoField(primary_key=True)
    disponible = models.CharField(max_length=1)
    id_pabellon = models.ForeignKey('Pabellon', models.CASCADE, db_column='id_pabellon')
    id_modulo = models.ForeignKey('Modulo', models.CASCADE, db_column='id_modulo')

    class Meta:
        managed = True
        db_table = 'disponibilidad_pabellon'
        verbose_name_plural = 'Disponibilidad pabellones'


class Evaluacion(models.Model):
    id_evaluacion = models.BigAutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.CASCADE, db_column='id_paciente')
    fecha = models.DateField()
    atencion = models.CharField(max_length=50)
    riesgo = models.DecimalField(max_digits=5, decimal_places=2)
    id_atencion = models.ForeignKey(Atencion, models.CASCADE, db_column='id_atencion')

    class Meta:
        managed = True
        db_table = 'evaluacion'
        unique_together = (('id_evaluacion', 'id_paciente'),)
        verbose_name_plural = 'Evaluaciones'


class Medico(models.Model):
    id_medico = models.BigAutoField(primary_key=True)
    rut = models.IntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    correo = models.CharField(max_length=200)
    password = models.CharField(max_length=2000)
    direccion = models.CharField(max_length=100)
    administrador = models.CharField(max_length=1)
    habilitado = models.CharField(max_length=1)
    id_cargo = models.ForeignKey(Cargo, models.CASCADE, db_column='id_cargo')
    id_ciudad = models.ForeignKey(Ciudad, models.CASCADE, db_column='id_ciudad')
    id_jefe = models.ForeignKey('self', models.CASCADE, db_column='id_jefe', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f'{self.rut}-{self.dv} / {self.nombre} {self.apellido_p}'


class Modulo(models.Model):
    id_modulo = models.BigAutoField(primary_key=True)
    hora_ini = models.DateField()
    hora_fin = models.DateField()

    class Meta:
        managed = True
        db_table = 'modulo'
        verbose_name_plural = 'Modulos'


class Pabellon(models.Model):
    id_pabellon = models.BigAutoField(primary_key=True)
    piso = models.IntegerField()
    numeracion = models.IntegerField()
    habilitado = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'pabellon'
        verbose_name_plural = 'Pabellones'


class Paciente(models.Model):
    id_paciente = models.BigAutoField(primary_key=True)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    correo = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'paciente'
        verbose_name_plural = 'Pacientes'


class ProgramacionCirugia(models.Model):
    id_reserva_cirugia = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    notificado = models.CharField(max_length=1)
    id_medico = models.ForeignKey(Medico, models.CASCADE, db_column='id_medico')
    id_evaluacion = models.ForeignKey(Evaluacion, models.CASCADE, db_column='id_evaluacion', related_name='id_evaluacion_related')
    id_paciente = models.ForeignKey(Evaluacion, models.CASCADE, db_column='id_paciente')
    id_detalle_unidad = models.ForeignKey(DetalleUnidad, models.CASCADE, db_column='id_detalle_unidad')

    class Meta:
        managed = True
        db_table = 'programacion_cirugia'
        verbose_name_plural = 'Programacion de cirugias'


class Recurso(models.Model):
    id_recurso = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad_actual = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    cantidad_peligro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recurso'
        verbose_name_plural = 'Recursos'


class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'region'
        verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.descripcion


class ReservaPabellon(models.Model):
    id_reserva = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    id_reserva_cirugia = models.OneToOneField(ProgramacionCirugia, models.CASCADE, db_column='id_reserva_cirugia')
    id_disponibilidad_pabellon = models.ForeignKey(DisponibilidadPabellon, models.CASCADE, db_column='id_disponibilidad_pabellon')

    class Meta:
        managed = True
        db_table = 'reserva_pabellon'
        verbose_name_plural = 'Reserva pabellones'


class ReservaRecurso(models.Model):
    id_reserva_recurso = models.BigAutoField(primary_key=True)
    cantidad = models.BigIntegerField()
    id_recurso = models.OneToOneField(Recurso, models.CASCADE, db_column='id_recurso')
    id_reserva = models.ForeignKey(ReservaPabellon, models.CASCADE, db_column='id_reserva')

    class Meta:
        managed = True
        db_table = 'reserva_recurso'
        unique_together = (('id_recurso', 'id_reserva'),)
        verbose_name_plural = 'Reserva recursos'


class Unidad(models.Model):
    id_unidad = models.BigAutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'unidad'
        verbose_name_plural = 'Unidades'