# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0008_auto_20150813_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_material',
            name='Calculo',
            field=models.CharField(choices=[(1, 'Laminados inelásticos'), (2, 'Laminados elásticos'), (3, 'Complementos')], max_length=200),
        ),
    ]
