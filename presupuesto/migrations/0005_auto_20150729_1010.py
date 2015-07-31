# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0004_presupuesto_detalle_descripcion_contenedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='descripcion_persona',
            field=models.TextField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='descripcion_vehiculo',
            field=models.TextField(default=0, blank=True),
        ),
    ]
