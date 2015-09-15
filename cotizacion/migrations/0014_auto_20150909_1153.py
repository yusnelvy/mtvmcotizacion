# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0013_vehiculo_cantidad_ayudante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_carga',
            name='cantidad_trabajador',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='nro_objeto_max',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='nro_objeto_min',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_max',
            field=models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0.001)], default=0.0, decimal_places=3, max_digits=8),
        ),
    ]
