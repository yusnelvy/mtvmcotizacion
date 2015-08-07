# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0007_auto_20150729_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='estado',
            field=models.CharField(max_length=20, default='Iniciado'),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='total_capacidad_vehiculo',
            field=models.DecimalField(blank=True, default=0.0, max_digits=7, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='total_peso_materiales',
            field=models.DecimalField(blank=True, default=0.0, max_digits=7, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='total_peso_mudanza',
            field=models.DecimalField(blank=True, default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(default=0, choices=[(10, 'De 1 metro a 10 metros'), (20, 'De 11 metros a 20 metros'), (30, 'De 21 metros a 30 metros'), (40, 'De 31 metros a 40 metros'), (50, 'De 41 metros a 50 metros'), (60, 'De 51 metros a 60 metros'), (60, 'Mas de 60 metros')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos',
            field=models.IntegerField(default=0, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor',
            field=models.IntegerField(default=0, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor_servicio',
            field=models.IntegerField(default=0, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_escalera',
            field=models.IntegerField(default=0, choices=[(0, '0'), (1, '1'), (2, '2'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(max_digits=5, default=0, choices=[(40, 'Entre 40 metros cuadrado'), (80, 'Entre 41 a 80 metros cuadrado'), (120, 'Entre 81 a 120 metros cuadrado'), (160, 'Entre 121 a 160 metros cuadrado'), (200, 'Entre 161 a 200 metros cuadrado'), (200, 'Mas de 200 metros cuadrado')], decimal_places=2),
        ),
    ]
