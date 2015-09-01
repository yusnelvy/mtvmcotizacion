# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0005_auto_20150810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_tipico',
            name='cantidad',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
