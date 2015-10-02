# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0036_datosprecargado_densidadcontenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosprecargado',
            name='densidadcontenido',
        ),
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='densidadcontenido',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=7),
            preserve_default=False,
        ),
    ]
