# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0030_auto_20150924_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='detalle_presupuesto',
            field=models.ForeignKey(to='presupuesto.Presupuesto_Detalle'),
        ),
    ]
