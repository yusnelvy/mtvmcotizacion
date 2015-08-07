# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0011_auto_20150805_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPrecargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('complejidadinmueble', models.CharField(max_length=100)),
                ('factorcomplejidadinmueble', models.DecimalField(max_digits=4, decimal_places=2)),
                ('valorambcompleinmueble', models.DecimalField(max_digits=13, decimal_places=2)),
                ('valorm3compleinmueble', models.DecimalField(max_digits=13, decimal_places=2)),
                ('ocupacioninmueble', models.CharField(max_length=100)),
                ('valorocupacioninmueble', models.DecimalField(max_digits=3, decimal_places=2)),
                ('densidadcontenidomueble', models.DecimalField(max_digits=5, decimal_places=2)),
                ('volcontenedormueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('peso_contenedormueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('capvolcontenedormueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('cappesocontenedormueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('tamanomueble', models.CharField(max_length=100)),
                ('densidadmueble', models.CharField(max_length=100)),
                ('anchomueble', models.DecimalField(max_digits=5, decimal_places=2)),
                ('largomueble', models.DecimalField(max_digits=5, decimal_places=2)),
                ('altomueble', models.DecimalField(max_digits=5, decimal_places=2)),
                ('pesomueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('valordensidadmueble', models.DecimalField(max_digits=5, decimal_places=2)),
                ('volumenmueble', models.DecimalField(max_digits=8, decimal_places=3)),
                ('tarifacomplejidadservicio', models.DecimalField(max_digits=13, decimal_places=2)),
                ('factortiempocompservicio', models.DecimalField(max_digits=7, decimal_places=5)),
                ('materialservicio', models.CharField(max_length=100)),
                ('preciomaterial', models.DecimalField(max_digits=7, decimal_places=2)),
                ('volmaterial', models.DecimalField(max_digits=8, decimal_places=3)),
                ('pesomaterial', models.DecimalField(max_digits=8, decimal_places=3)),
            ],
            options={
                'verbose_name': 'Dato Precargado',
                'verbose_name_plural': 'Datos Precargados',
            },
        ),
    ]
