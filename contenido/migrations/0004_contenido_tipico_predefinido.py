# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_auto_20150623_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido_tipico',
            name='predefinido',
            field=models.BooleanField(default=False),
        ),
    ]
