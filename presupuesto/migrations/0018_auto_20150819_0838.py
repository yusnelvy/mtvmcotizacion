# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0017_auto_20150818_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='monto_persona',
            new_name='monto_personaoptima',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='duracion_optima',
            field=models.DecimalField(default='0.00', max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_personateorica',
            field=models.DecimalField(default=0.0, max_digits=9, decimal_places=2, blank=True),
        ),
    ]
