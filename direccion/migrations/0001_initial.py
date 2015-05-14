# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ciudad', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complejidad_Inmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('complejidad', models.CharField(max_length=100)),
                ('factor', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'verbose_name': 'complejidad del inmueble',
                'verbose_name_plural': 'complejidades del inmuebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('piso', models.CharField(max_length=100)),
                ('adicional', models.CharField(max_length=250)),
                ('zip1', models.CharField(max_length=100)),
                ('punto_referencia', models.CharField(max_length=250)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('inmueble', models.CharField(max_length=100)),
                ('numero_ambientes', models.IntegerField()),
                ('pisos', models.IntegerField()),
                ('pisos_escalera', models.IntegerField()),
                ('rampa', models.BooleanField(default=False)),
                ('ascensor', models.BooleanField(default=False)),
                ('ascensor_servicio', models.BooleanField(default=False)),
                ('pisos_ascensor_servicio', models.IntegerField()),
                ('pisos_ascensor', models.IntegerField()),
                ('distancia_vehiculo', models.IntegerField()),
                ('complejidad', models.ForeignKey(to='direccion.Complejidad_Inmueble')),
                ('direccion', models.ForeignKey(to='direccion.Direccion')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pais', models.CharField(unique=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('provincia', models.CharField(unique=True, max_length=100)),
                ('pais', models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_direccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tipo_direccion', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo de direccion',
                'verbose_name_plural': 'Tipos de direccion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Inmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tipo_inmueble', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo inmueble',
                'verbose_name_plural': 'Tipo inmuebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('zona', models.CharField(unique=True, max_length=100)),
                ('cuidad', models.ForeignKey(to='direccion.Ciudad')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='tipo_inmueble',
            field=models.ForeignKey(to='direccion.Tipo_Inmueble'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='tipo_direccion',
            field=models.ForeignKey(to='direccion.Tipo_direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='zona',
            field=models.ForeignKey(to='direccion.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(to='direccion.Provincia'),
            preserve_default=True,
        ),
    ]
