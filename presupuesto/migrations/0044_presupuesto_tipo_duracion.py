# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0043_datosprecargado_porcentaje_variacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='tipo_duracion',
            field=models.CharField(max_length=20, default='Optimizado'),
        ),
    ]
