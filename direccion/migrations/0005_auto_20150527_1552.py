# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0004_auto_20150522_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complejidad_inmueble',
            options={'verbose_name_plural': 'complejidades del inmueble', 'verbose_name': 'complejidad del inmueble'},
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='complejidad_inmueble',
            name='complejidad',
            field=models.CharField(max_length=100, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='adicional',
            field=models.CharField(blank=True, max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_direccion',
            name='tipo_direccion',
            field=models.CharField(max_length=10, unique=True),
            preserve_default=True,
        ),
    ]
