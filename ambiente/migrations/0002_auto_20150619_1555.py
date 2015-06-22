# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ambiente_tipo_inmueble',
            unique_together=set([('ambiente', 'tipo_inmueble')]),
        ),
    ]
