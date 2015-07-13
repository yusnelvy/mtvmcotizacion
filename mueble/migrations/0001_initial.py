# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Densidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Densidades',
                'verbose_name': 'Densidad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Forma_Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('forma', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['forma'],
                'verbose_name_plural': 'Formas del Mueble',
                'verbose_name': 'Forma del Mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('mueble', models.CharField(max_length=100, unique=True)),
                ('capacidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('trasladable', models.BooleanField(default=None)),
                ('apilable', models.BooleanField(default=None)),
                ('capacidad_carga', models.BooleanField(default=None)),
                ('capacidad_interna', models.BooleanField(default=None)),
                ('forma', models.ForeignKey(to='mueble.Forma_Mueble')),
            ],
            options={
                'ordering': ['mueble'],
                'verbose_name_plural': 'Muebles',
                'verbose_name': 'Mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mueble_Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('predefinido', models.BooleanField(default=None)),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('mueble', models.ForeignKey(to='mueble.Mueble')),
            ],
            options={
                'ordering': ['ambiente', 'mueble'],
                'verbose_name_plural': 'Muebles  del Ambiente',
                'verbose_name': 'Mueble del Ambiente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('valor', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Ocupaciones',
                'verbose_name': 'Ocupacion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Tamanos',
                'verbose_name': 'Tamano',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamano_Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ancho', models.DecimalField(max_digits=5, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=5, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=5, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('predefinido', models.BooleanField(default=None)),
                ('densidad', models.ForeignKey(to='mueble.Densidad', on_delete=django.db.models.deletion.PROTECT)),
                ('mueble', models.ForeignKey(to='mueble.Mueble', on_delete=django.db.models.deletion.PROTECT)),
                ('tamano', models.ForeignKey(to='mueble.Tamano', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['mueble', 'tamano', 'densidad'],
                'verbose_name_plural': 'Tamanos del mueble',
                'verbose_name': 'Tamano del mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo_mueble', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['tipo_mueble'],
                'verbose_name_plural': 'Tipos de mueble',
                'verbose_name': 'Tipo mueble',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mueble',
            name='ocupacion',
            field=models.ForeignKey(to='mueble.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mueble',
            name='tipo_mueble',
            field=models.ForeignKey(to='mueble.Tipo_Mueble'),
            preserve_default=True,
        ),
    ]
