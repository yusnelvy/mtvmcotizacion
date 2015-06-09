# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0005_auto_20150608_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocupacion',
            name='valor',
            field=models.DecimalField(max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
