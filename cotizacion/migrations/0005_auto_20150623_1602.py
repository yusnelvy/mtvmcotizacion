# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_auto_20150622_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion_servicio',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='cotizacion_contenido',
            field=models.ForeignKey(null=True, blank=True, to='cotizacion.Cotizacion_Contenido'),
            preserve_default=True,
        ),
    ]
