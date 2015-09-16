# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0025_auto_20150915_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='monto_descuesto_regargo',
            new_name='monto_descuento_regargo',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='descuento_recargo',
            field=models.CharField(default='-', max_length=1),
            preserve_default=False,
        ),
    ]
