# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0031_auto_20150924_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto_servicio',
            name='unidad_material',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
