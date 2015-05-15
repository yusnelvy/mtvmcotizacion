# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complejidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Complejidad',
                'verbose_name_plural': 'Complejidades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complejidad_Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tarifa', models.DecimalField(max_digits=13, decimal_places=2)),
                ('complejidad', models.ForeignKey(to='servicio.Complejidad')),
            ],
            options={
                'verbose_name': 'Complejidad del Servicio',
                'verbose_name_plural': 'Complejidades del Servicio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('material', models.CharField(max_length=100)),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('recuperable', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('servicio', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio_Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('material', models.ForeignKey(to='servicio.Material')),
                ('servicio', models.ForeignKey(to='servicio.Servicio')),
            ],
            options={
                'verbose_name': 'Material del Servicio',
                'verbose_name_plural': 'Materiales del Servicio',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='complejidad_servicio',
            name='servicio',
            field=models.ForeignKey(to='servicio.Servicio'),
            preserve_default=True,
        ),
    ]
