# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0005_complejidad_servicio_factor_tiempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='capacidad_peso',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='material',
            name='capacidad_volumen',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='material',
            name='peso',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
    ]
