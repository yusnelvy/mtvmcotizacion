# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20150527_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado_cotizacion',
            options={'verbose_name': 'estado', 'verbose_name_plural': 'estados'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos', 'ordering': ['-tarifa_hora']},
        ),
    ]
