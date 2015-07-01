# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_auto_20150623_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion_servicio',
            name='complejidad',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_servicio',
            name='tarifa',
            field=models.DecimalField(max_digits=13, default=1, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='porcentaje',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
