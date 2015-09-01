# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0021_auto_20150826_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='monto_descuesto_regargo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
