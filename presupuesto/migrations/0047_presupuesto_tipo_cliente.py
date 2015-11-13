# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0046_remove_presupuesto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='tipo_cliente',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
    ]
