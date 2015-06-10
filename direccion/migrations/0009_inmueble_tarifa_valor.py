# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0008_tarifa_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='tarifa_valor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='direccion.Tarifa_valor'),
            preserve_default=False,
        ),
    ]
