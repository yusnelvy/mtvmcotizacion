# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0032_presupuesto_servicio_unidad_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto_detalle',
            name='densidad',
        ),
        migrations.RemoveField(
            model_name='presupuesto_detalle',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='presupuesto_detalle',
            name='valor_densidad',
        ),
    ]
