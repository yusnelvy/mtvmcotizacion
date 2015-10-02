# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0035_auto_20151001_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosprecargado',
            name='densidadcontenido',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
            preserve_default=False,
        ),
    ]
