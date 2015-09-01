# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0010_auto_20150813_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_material',
            name='calculo',
            field=models.CharField(choices=[('1', 'Laminados inelásticos'), ('2', 'Laminados elásticos'), ('3', 'Complementos'), ('4', 'Contenedor')], max_length=200),
        ),
        migrations.AlterField(
            model_name='servicio_material',
            name='cantidad',
            field=models.DecimalField(max_digits=7, decimal_places=2, default='1.00'),
        ),
    ]
