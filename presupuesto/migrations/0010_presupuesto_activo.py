# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0009_presupuesto_total_volumen_materiales'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='activo',
            field=models.CharField(max_length=20, default='Activado'),
        ),
    ]
