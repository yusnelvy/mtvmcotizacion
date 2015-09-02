# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0020_presupuesto_detalle_trasladable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='total_capacidad_vehiculo',
            new_name='total_capacidad_vehiculokg',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='total_capacidad_vehiculovol',
            field=models.DecimalField(max_digits=8, decimal_places=3, default=0.0, blank=True),
        ),
    ]
