# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0018_auto_20150819_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='cantidad_persona',
        ),
    ]
