# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0002_auto_20150619_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='densidad',
            options={'ordering': ['id'], 'verbose_name': 'Densidad', 'verbose_name_plural': 'Densidades'},
        ),
    ]
