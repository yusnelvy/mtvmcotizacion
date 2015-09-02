# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0015_auto_20150813_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosprecargado',
            name='duracion_optimamudanza',
            field=models.DecimalField(max_digits=7, decimal_places=2, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='rendimiento_peso',
            field=models.DecimalField(max_digits=9, decimal_places=3, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='rendimiento_unidad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='rendimiento_volumen',
            field=models.DecimalField(max_digits=8, decimal_places=3, default=0),
            preserve_default=False,
        ),
    ]
