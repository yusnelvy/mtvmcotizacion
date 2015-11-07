# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0042_presupuesto_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosprecargado',
            name='porcentaje_variacion',
            field=models.DecimalField(max_digits=8, default=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
