# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='recuperable',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
