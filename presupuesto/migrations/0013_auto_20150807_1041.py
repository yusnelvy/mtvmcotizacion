# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0012_datosprecargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosprecargado',
            name='cantidadmaterial',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='montomaterial',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
    ]
