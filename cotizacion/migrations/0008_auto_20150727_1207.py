# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0007_auto_20150710_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cantidad_disponible',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='cantidad_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
