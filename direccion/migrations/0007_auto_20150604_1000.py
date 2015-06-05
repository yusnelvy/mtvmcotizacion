# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0006_auto_20150602_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_direccion',
            name='tipo_direccion',
            field=models.CharField(max_length=50, unique=True),
            preserve_default=True,
        ),
    ]
