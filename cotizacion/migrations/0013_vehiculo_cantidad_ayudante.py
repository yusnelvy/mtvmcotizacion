# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0012_auto_20150813_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cantidad_ayudante',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
