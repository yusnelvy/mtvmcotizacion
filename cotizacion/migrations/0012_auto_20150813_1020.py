# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0011_auto_20150813_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo_carga',
            name='volumen_max',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=8, blank=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0.001)]),
        ),
    ]
