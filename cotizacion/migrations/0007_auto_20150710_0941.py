# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0006_auto_20150630_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='inmueble',
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='ascensor',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='ascensor_servicio',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='complejidad',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='distancia_vehiculo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='inmueble',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='pisos',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='pisos_ascensor',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='pisos_ascensor_servicio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='pisos_escalera',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='rampa',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='tipo_inmueble',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_direccion',
            name='total_m2',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
