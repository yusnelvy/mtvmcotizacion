# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0005_auto_20150729_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto_servicio',
            name='tiempo_aplicado',
            field=models.TimeField(default='00:00'),
        ),
    ]
