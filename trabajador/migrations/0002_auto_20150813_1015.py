# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo_trabajador',
            name='recargo_fin_semana',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cargo_trabajador',
            name='recargo_nocturno',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cargo_trabajador',
            name='tarifa_dia',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
