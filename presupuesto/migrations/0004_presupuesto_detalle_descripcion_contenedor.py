# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0003_presupuesto_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='descripcion_contenedor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
