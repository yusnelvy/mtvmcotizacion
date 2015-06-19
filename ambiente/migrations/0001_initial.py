# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ambiente', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['ambiente'],
                'verbose_name_plural': 'Ambientes',
                'verbose_name': 'Ambiente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ambiente_Tipo_inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('tipo_inmueble', models.ForeignKey(to='direccion.Tipo_Inmueble')),
            ],
            options={
                'ordering': ['tipo_inmueble', 'ambiente'],
                'verbose_name_plural': 'Ambientes por tipos de inmueble',
                'verbose_name': 'Ambiente por tipo inmueble',
            },
            bases=(models.Model,),
        ),
    ]
