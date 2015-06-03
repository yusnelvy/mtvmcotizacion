# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0003_auto_20150527_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complejidad',
            options={'verbose_name': 'Nivel de complejidad', 'verbose_name_plural': 'Niveles de complejidad', 'ordering': ['id']},
        ),
    ]
