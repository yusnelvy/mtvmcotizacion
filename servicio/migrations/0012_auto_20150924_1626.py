# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0011_auto_20150818_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='nrovuelta',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='material',
            name='solape',
            field=models.DecimalField(default='0.20', decimal_places=2, max_digits=7),
        ),
    ]
