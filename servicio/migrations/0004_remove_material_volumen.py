# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0003_material_unidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='volumen',
        ),
    ]
