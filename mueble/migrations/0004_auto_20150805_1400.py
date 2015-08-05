# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0003_auto_20150713_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamano_mueble',
            name='peso',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
    ]
