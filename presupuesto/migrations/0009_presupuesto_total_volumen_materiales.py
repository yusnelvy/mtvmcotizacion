# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0008_auto_20150731_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='total_volumen_materiales',
            field=models.DecimalField(blank=True, max_digits=7, default=0.0, decimal_places=2),
        ),
    ]
