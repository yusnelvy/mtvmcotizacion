# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0005_auto_20150810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='capacidad',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='alto',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='ancho',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='largo',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
