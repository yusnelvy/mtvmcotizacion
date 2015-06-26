# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20150619_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unidad',
            field=models.ForeignKey(default=1, to='servicio.Unidad'),
            preserve_default=False,
        ),
    ]
