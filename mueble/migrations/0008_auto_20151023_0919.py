# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0007_auto_20150930_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='capacidad',
            field=models.DecimalField(decimal_places=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], max_digits=8),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='valor',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], max_digits=5),
        ),
    ]
