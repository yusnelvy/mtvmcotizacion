# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0006_auto_20150813_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_tipico',
            name='cantidad',
            field=models.DecimalField(decimal_places=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], max_digits=8),
        ),
    ]
