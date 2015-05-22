# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forma_Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('forma', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Formas del Mueble',
                'verbose_name': 'Forma del Mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('mueble', models.CharField(max_length=100)),
                ('capacidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('trasladable', models.BooleanField(default=None)),
                ('apilable', models.BooleanField(default=None)),
                ('capacidad_carga', models.BooleanField(default=None)),
                ('capacidad_interna', models.BooleanField(default=None)),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('forma', models.ForeignKey(to='mueble.Forma_Mueble')),
            ],
            options={
                'verbose_name_plural': 'Muebles',
                'verbose_name': 'Mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mueble_Ambiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('mueble', models.ForeignKey(to='mueble.Mueble')),
            ],
            options={
                'verbose_name_plural': 'Muebles  del Ambiente',
                'verbose_name': 'Mueble del Ambiente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('valor', models.DecimalField(max_digits=2, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Ocupaciones',
                'verbose_name': 'Ocupacion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tamanos',
                'verbose_name': 'Tamano',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamano_Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ancho', models.DecimalField(max_digits=2, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=2, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=2, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=2, decimal_places=2)),
                ('predefinido', models.BooleanField(default=None)),
                ('mueble', models.ForeignKey(to='mueble.Mueble')),
                ('tamano', models.ForeignKey(to='mueble.Tamano')),
            ],
            options={
                'verbose_name_plural': 'Tamanos del mueble',
                'verbose_name': 'Tamano mueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tipo_mueble', models.CharField(max_length=100)),
            ],
            options={
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
