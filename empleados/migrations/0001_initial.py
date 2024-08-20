# Generated by Django 5.0.3 on 2024-04-26 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0006_rename_persona_perfil_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('Per_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Per_tipoId', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('CE', 'Cedula de Extranjeria'), ('PA', 'Pasaporte')], max_length=30, verbose_name='Tipo de identificacion')),
                ('Per_id', models.CharField(max_length=50, verbose_name='Identificacion')),
                ('Per_nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Per_apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('Per_correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo')),
                ('Per_telefono', models.IntegerField(verbose_name='Telefono')),
                ('Mun_nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('Emp_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Emp_cargo', models.CharField(max_length=60, verbose_name='cargo')),
                ('Emp_salario', models.IntegerField(verbose_name='salario')),
                ('Emp_fechaingreso', models.DateField(auto_now_add=True, verbose_name='fecha de ingreso')),
                ('Per_nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.persona')),
            ],
        ),
    ]
