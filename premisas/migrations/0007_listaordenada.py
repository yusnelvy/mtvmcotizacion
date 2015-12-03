# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0006_auto_20151019_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaOrdenada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('id_item', models.IntegerField()),
                ('modulo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Listas Ordenadas',
                'verbose_name': 'Lista Ordenada',
            },
        ),
    ]
