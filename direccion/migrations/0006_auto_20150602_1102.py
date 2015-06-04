# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0005_auto_20150527_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
