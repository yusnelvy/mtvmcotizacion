# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0005_auto_20150810_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='total_m2',
            field=models.DecimalField(decimal_places=2, max_digits=7, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complejidad_inmueble',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='complejidad_inmueble',
            name='valor_ambiente',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='complejidad_inmueble',
            name='valor_metrocubico',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
