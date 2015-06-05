# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0002_auto_20150527_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamano_mueble',
            name='alto',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='ancho',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='largo',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
    ]
