# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20150623_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmueble',
            name='tarifa_valor',
        ),
        migrations.DeleteModel(
            name='Tarifa_valor',
        ),
        migrations.AddField(
            model_name='complejidad_inmueble',
            name='valor_ambiente',
            field=models.DecimalField(max_digits=13, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complejidad_inmueble',
            name='valor_metrocubico',
            field=models.DecimalField(max_digits=13, decimal_places=2, default=1),
            preserve_default=False,
        ),
    ]
