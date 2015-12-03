# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0008_auto_20151023_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamano_mueble',
            name='tamano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Tamano', default=1),
        ),
    ]
