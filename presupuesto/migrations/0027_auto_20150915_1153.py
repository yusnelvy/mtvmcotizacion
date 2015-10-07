# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0026_auto_20150915_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='monto_descuento_regargo',
            new_name='monto_descuento_recargo',
        ),
    ]
