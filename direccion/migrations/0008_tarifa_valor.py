# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0007_auto_20150604_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa_valor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
                ('valor', models.DecimalField(max_digits=13, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Tarifa del inmueble',
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Tarifas del inmueble',
            },
            bases=(models.Model,),
        ),
    ]
