# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0008_auto_20150727_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_max',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='tiempo_carga',
            name='peso_min',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='capacidad_peso',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='capacidad_volumen',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
    ]
