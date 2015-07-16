# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto_direccion',
            name='inmueble',
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_con_impuesto',
            field=models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='recorrido_km',
            field=models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_carga',
            field=models.TimeField(blank=True, default='00:00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.TimeField(blank=True, default='00:00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_total',
            field=models.TimeField(blank=True, default='00:00'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_m3',
            field=models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_ascensor_servicio',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='pisos_escalera',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
