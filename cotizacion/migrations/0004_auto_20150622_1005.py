# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0003_auto_20150622_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='cotizacion_contenido',
            field=models.ForeignKey(to='contenido.Contenido', blank=True, null=True),
            preserve_default=True,
        ),
    ]
