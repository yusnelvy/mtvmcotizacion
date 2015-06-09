# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0004_auto_20150608_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tamano_mueble',
            options={'ordering': ['mueble', 'tamano', 'densidad'], 'verbose_name': 'Tamano del mueble', 'verbose_name_plural': 'Tamanos del mueble'},
        ),
        migrations.AddField(
            model_name='tamano_mueble',
            name='densidad',
            field=models.ForeignKey(to='mueble.Densidad', default=1, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=False,
        ),
    ]
