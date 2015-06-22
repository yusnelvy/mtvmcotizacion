# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo_trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cargo', models.CharField(max_length=100, unique=True)),
                ('tarifa_dia', models.DecimalField(max_digits=7, decimal_places=2)),
                ('recargo_fin_semana', models.DecimalField(max_digits=7, decimal_places=2)),
                ('recargo_nocturno', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'ordering': ['cargo'],
                'verbose_name_plural': 'Cargos de trabajadores',
                'verbose_name': 'Cargo de trabajador',
            },
            bases=(models.Model,),
        ),
    ]
