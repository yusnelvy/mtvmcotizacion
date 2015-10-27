# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0045_auto_20151027_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='estado',
        ),
    ]
