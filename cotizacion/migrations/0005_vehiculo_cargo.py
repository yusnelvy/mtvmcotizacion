# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0002_auto_20150527_1552'),
        ('cotizacion', '0004_auto_20150604_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cargo',
            field=models.ForeignKey(to='trabajador.Cargo_trabajador', default=1),
            preserve_default=False,
        ),
    ]
