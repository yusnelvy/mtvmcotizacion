# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telefono', '0002_auto_20150515_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telefono',
            options={'verbose_name_plural': 'Telefonos', 'ordering': ['numero'], 'verbose_name': 'Telefono'},
        ),
        migrations.AlterModelOptions(
            name='tipo_telefono',
            options={'verbose_name_plural': 'Tipos de telefono', 'ordering': ['tipo_telefono'], 'verbose_name': 'Tipo de telefono'},
        ),
        migrations.AlterField(
            model_name='tipo_telefono',
            name='tipo_telefono',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
