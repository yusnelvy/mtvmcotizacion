# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('contenedor', models.CharField(max_length=100, unique=True)),
                ('capacidad_volumen', models.DecimalField(max_digits=5, decimal_places=2)),
                ('capacidad_peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('volumen_contenedor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('peso_contenedor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('retornable', models.BooleanField(default=None)),
            ],
            options={
                'ordering': ['contenedor'],
                'verbose_name_plural': 'contenedores',
                'verbose_name': 'contenedor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('contenido', models.CharField(max_length=100, unique=True)),
                ('densidad_baja', models.DecimalField(max_digits=7, decimal_places=2)),
                ('densidad_media', models.DecimalField(max_digits=7, decimal_places=2)),
                ('densidad_alta', models.DecimalField(max_digits=7, decimal_places=2)),
                ('densidad_superalta', models.DecimalField(max_digits=7, decimal_places=2)),
                ('contenedor', models.ForeignKey(to='contenido.Contenedor')),
            ],
            options={
                'ordering': ['contenido'],
                'verbose_name_plural': 'contenidos',
                'verbose_name': 'contenido',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contenido_Tipico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(max_digits=2, decimal_places=2)),
                ('contenido', models.ForeignKey(to='contenido.Contenido')),
                ('mueble', models.ForeignKey(to='mueble.Mueble')),
            ],
            options={
                'ordering': ['mueble', 'contenido'],
                'verbose_name_plural': 'Contenidos Tipicos',
                'verbose_name': 'Contenido Tipico',
            },
            bases=(models.Model,),
        ),
    ]
