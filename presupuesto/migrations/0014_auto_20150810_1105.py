# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0013_auto_20150807_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(max_digits=7, default=5.0, choices=[(20.0, 'Entre 1 KM a 20 KM'), (40.0, 'Entre 21 KM a 40 KM'), (60.0, 'Entre 41 KM a 60 KM'), (80.0, 'Entre 61 KM a 80 KM'), (100.0, 'Entre 81 KM a 100 KM'), (120.0, 'Entre 101 KM a 120 KM'), (140.0, 'Entre 121 KM a 140 KM'), (160.0, 'Entre 141 KM a 160 KM'), (180.0, 'Entre 161 KM a 180 KM'), (200.0, 'Más de 200 KM')], decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(max_digits=5, default=1.0, choices=[(1.0, 'Entre 30 minuto a 1 hora'), (2.0, 'Entre 1 hora a 2 horas'), (3.0, 'Entre 2 horas a 3 horas'), (4.0, 'Entre 3 horas a 4 horas'), (5.0, 'Entre 4 horas a 5 horas'), (6.0, 'Entre 5 horas a 6 horas'), (7.0, 'Entre 6 horas a 7 horas'), (8.0, 'Entre 7 horas a 8 horas'), (9.0, 'Entre 8 horas a 9 horas'), (10.0, 'Más de 10 horas')], decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='presupuesto.Presupuesto'),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor',
            field=models.IntegerField(default=0, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor_servicio',
            field=models.IntegerField(default=0, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_escalera',
            field=models.IntegerField(default=0, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10 o más')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='presupuesto.Presupuesto'),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='detalle_presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='presupuesto.Presupuesto_Detalle'),
        ),
    ]
