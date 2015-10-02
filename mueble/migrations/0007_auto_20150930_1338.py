# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0006_auto_20150813_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tamano_mueble',
            options={'verbose_name_plural': 'Tamanos del mueble', 'ordering': ['mueble', 'tamano'], 'verbose_name': 'Tamano del mueble'},
        ),
        migrations.AlterUniqueTogether(
            name='tamano_mueble',
            unique_together=set([('tamano', 'mueble')]),
        ),
        migrations.RemoveField(
            model_name='tamano_mueble',
            name='densidad',
        ),
        migrations.RemoveField(
            model_name='tamano_mueble',
            name='peso',
        ),
    ]
