# Generated by Django 4.1.7 on 2023-06-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_publicacion_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='asunto',
            field=models.CharField(choices=[('ayuda', 'Ayuda en una asignatura'), ('debate', 'Debate sobre una materia'), ('problema', 'Problema en la sede'), ('otros', 'Otros')], max_length=100),
        ),
    ]
