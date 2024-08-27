# Generated by Django 5.0.3 on 2024-08-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0009_alter_empleado_emp_subtipotrabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='Emp_banco',
            field=models.IntegerField(choices=[(1, 'Bancamía'), (2, 'Bancolombia'), (3, 'Bancoomeva'), (4, 'Banco agrario'), (5, 'Banco av villas'), (6, 'Banco caja social'), (7, 'Banco credifinanciera'), (8, 'Banco de bogotá'), (9, 'Banco de occidente'), (10, 'Banco falabella'), (11, 'Banco finandina'), (12, 'Banco GNB Sudameris'), (13, 'Banco J.P. MORGAN'), (14, 'Banco mundo mujer'), (15, 'Banco NU'), (16, 'Banco pichincha'), (17, 'Banco popular'), (18, 'Banco santander'), (19, 'Banco serfinanza'), (20, 'Banco W'), (21, 'BBVA'), (22, 'Citibank'), (23, 'Coopcentral'), (24, 'Cooperativa confiar'), (25, 'Cooperativa cootramed'), (26, 'Cooperativa cotrafa'), (27, 'Cooperativa de ahorro y crédito nacional'), (28, 'Cooperativa financiera de antioquia'), (29, 'Cooperativa utrahuilca'), (30, 'Cooprofesores'), (31, 'Davivienda'), (32, 'Daviplata'), (33, 'Mibanco'), (34, 'Nequi'), (35, 'Itaú'), (36, 'Scotibank colpatria'), (37, 'Juriscoop'), (38, 'DALE'), (39, 'Crediflores'), (40, 'Lulo Bank'), (41, 'Global66'), (42, 'RappiPay')], default=1, max_length=60, verbose_name='Banco'),
            preserve_default=False,
        ),
    ]
