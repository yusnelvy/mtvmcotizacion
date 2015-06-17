# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20150605_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado_civil',
            field=models.ForeignKey(to='cliente.Estado_civil', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.ForeignKey(to='cliente.Sexo', default=1),
            preserve_default=False,
        ),
    ]
