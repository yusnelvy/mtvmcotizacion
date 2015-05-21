# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido_Tipico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('cantidad', models.DecimalField(max_digits=2, decimal_places=2)),
                ('contenido', models.ForeignKey(to='contenido.Contenido')),
            ],
            options={
                'verbose_name_plural': 'Contenidos Tipicos',
                'verbose_name': 'Contenido Tipico',
            },
            bases=(models.Model,),
        ),
    ]
