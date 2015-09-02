# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0019_remove_presupuesto_cantidad_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='trasladable',
            field=models.BooleanField(default=None),
        ),
    ]
