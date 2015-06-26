# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_auto_20150619_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_tipico',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
    ]
