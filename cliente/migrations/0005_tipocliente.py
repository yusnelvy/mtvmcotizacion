# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20150810_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tipo_cliente', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['tipo_cliente'],
                'verbose_name': 'Tipo de cliente',
                'verbose_name_plural': 'Tipos de cliente',
            },
        ),
    ]
