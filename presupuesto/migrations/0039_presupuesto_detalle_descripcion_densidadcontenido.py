# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0038_auto_20151001_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='descripcion_densidadcontenido',
            field=models.CharField(max_length=100, default='Media'),
            preserve_default=False,
        ),
    ]
