# Generated by Django 4.1.7 on 2023-06-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_carrera_comentario_docente_escuela_estudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]