# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20150619_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='cotizacion_contenido',
            field=models.ForeignKey(to='contenido.Contenido', blank=True),
            preserve_default=True,
        ),
    ]
