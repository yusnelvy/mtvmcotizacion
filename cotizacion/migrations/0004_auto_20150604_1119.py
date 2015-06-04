# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0003_auto_20150602_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado_cotizacion',
            options={'ordering': ['id'], 'verbose_name': 'estado', 'verbose_name_plural': 'estados'},
        ),
    ]
