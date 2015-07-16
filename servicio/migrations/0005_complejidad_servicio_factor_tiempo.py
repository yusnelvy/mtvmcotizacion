# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_remove_material_volumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='complejidad_servicio',
            name='factor_tiempo',
            field=models.DecimalField(max_digits=7, decimal_places=2, default=1),
            preserve_default=False,
        ),
    ]
