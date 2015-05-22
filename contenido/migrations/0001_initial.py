# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('contenedor', models.CharField(max_length=100)),
                ('capacidad_volumen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('capacidad_peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volumen_contenedor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_contenedor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('retornable', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'contenedor',
                'verbose_name_plural': 'contenedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=100)),
                ('densidad_baja', models.DecimalField(decimal_places=2, max_digits=5)),
                ('densidad_media', models.DecimalField(decimal_places=2, max_digits=5)),
                ('densidad_alta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('densidad_superalta', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'contenido',
                'verbose_name_plural': 'contenidos',
            },
            bases=(models.Model,),
        ),
    ]
