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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Niveles de complejidad',
                'verbose_name': 'Nivel de complejidad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complejidad_Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tarifa', models.DecimalField(max_digits=13, decimal_places=2)),
                ('complejidad', models.ForeignKey(to='servicio.Complejidad')),
            ],
            options={
                'ordering': ['servicio', 'complejidad'],
                'verbose_name_plural': 'Complejidades del Servicio',
                'verbose_name': 'Complejidad del Servicio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('material', models.CharField(max_length=100, unique=True)),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('recuperable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['material'],
                'verbose_name_plural': 'Materiales',
                'verbose_name': 'Material',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('servicio', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['servicio'],
                'verbose_name_plural': 'servicios',
                'verbose_name': 'servicio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('Calculo', models.TextField(max_length=200)),
                ('material', models.ForeignKey(to='servicio.Material')),
                ('servicio', models.ForeignKey(to='servicio.Servicio')),
            ],
            options={
                'ordering': ['servicio', 'material'],
                'verbose_name_plural': 'Materiales del Servicio',
                'verbose_name': 'Material del Servicio',
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
