# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0029_auto_20150922_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='comentario',
            field=models.TextField(blank=True),
        ),
    ]
