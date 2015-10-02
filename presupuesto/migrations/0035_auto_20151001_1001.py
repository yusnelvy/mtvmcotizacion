# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0034_auto_20150930_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosprecargado',
            name='descripcioncontenedor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosprecargado',
            name='descripcioncontenido',
            field=models.CharField(default='No definido', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto_detalle',
            name='descripcion_contenido',
            field=models.CharField(default='No definido', max_length=100),
            preserve_default=False,
        ),
    ]
