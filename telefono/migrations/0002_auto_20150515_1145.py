# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telefono', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_telefono',
            options={'verbose_name_plural': 'Tipos de telefono'},
        ),
        migrations.AlterField(
            model_name='telefono',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
    ]
