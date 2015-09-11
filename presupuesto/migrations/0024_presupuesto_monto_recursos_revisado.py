# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0023_auto_20150909_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='monto_recursos_revisado',
            field=models.DecimalField(max_digits=9, blank=True, decimal_places=2, default=0.0),
        ),
    ]
