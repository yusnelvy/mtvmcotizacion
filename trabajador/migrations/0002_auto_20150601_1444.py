# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo_trabajador',
            options={'verbose_name_plural': 'Cargos de trabajadores', 'ordering': ['cargo'], 'verbose_name': 'Cargo de trabajador'},
        ),
        migrations.AlterField(
            model_name='cargo_trabajador',
            name='cargo',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
