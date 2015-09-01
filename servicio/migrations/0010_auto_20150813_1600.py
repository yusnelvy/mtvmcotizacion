# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_auto_20150813_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio_material',
            name='Calculo',
        ),
        migrations.AddField(
            model_name='servicio_material',
            name='calculo',
            field=models.CharField(max_length=200, choices=[('1', 'Laminados inelásticos'), ('2', 'Laminados elásticos'), ('3', 'Complementos')], default=1),
            preserve_default=False,
        ),
    ]
