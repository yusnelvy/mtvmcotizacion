# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_vehiculo_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiempo_carga',
            name='cantidad_trabajador',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
