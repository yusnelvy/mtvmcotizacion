# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0012_auto_20150924_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_material',
            name='calculo',
            field=models.CharField(choices=[('', 'Seleccione la forma de cálculo'), ('1', 'Laminados inelásticos'), ('2', 'Laminados elásticos'), ('3', 'Complementos'), ('4', 'Contenedor')], max_length=200),
        ),
    ]
