# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20150710_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Estado_civil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Sexo'),
        ),
    ]
