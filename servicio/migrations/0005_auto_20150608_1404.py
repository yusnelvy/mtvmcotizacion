# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_auto_20150602_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio_material',
            name='Calculo',
            field=models.TextField(max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio_material',
            name='cantidad',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
    ]
