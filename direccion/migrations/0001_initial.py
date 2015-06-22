# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ciudad', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['provincia', 'ciudad'],
                'verbose_name_plural': 'Ciudades',
                'verbose_name': 'Ciudad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complejidad_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('complejidad', models.CharField(max_length=100, unique=True)),
                ('factor', models.DecimalField(max_digits=2, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'complejidades del inmueble',
                'verbose_name': 'complejidad del inmueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('piso', models.CharField(max_length=100)),
                ('adicional', models.CharField(max_length=250, blank=True)),
                ('zip1', models.CharField(max_length=100)),
                ('punto_referencia', models.CharField(max_length=250)),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_field='provincia', chained_model_field='provincia', to='direccion.Ciudad')),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'ordering': ['tipo_direccion'],
                'verbose_name_plural': 'Direcciones',
                'verbose_name': 'Direccion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('complejidad', models.ForeignKey(to='direccion.Complejidad_Inmueble', on_delete=django.db.models.deletion.PROTECT)),
                ('direccion', models.ForeignKey(to='direccion.Direccion', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['inmueble'],
                'verbose_name_plural': 'Inmuebles',
                'verbose_name': 'Inmueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='locaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_field='provincia', chained_model_field='provincia', to='direccion.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pais', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ['pais'],
                'verbose_name_plural': 'Paises',
                'verbose_name': 'Pais',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('provincia', models.CharField(max_length=100, unique=True)),
                ('pais', models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['pais', 'provincia'],
                'verbose_name_plural': 'Provincias',
                'verbose_name': 'Provincia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarifa_valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('valor', models.DecimalField(max_digits=13, decimal_places=2)),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Tarifas del inmueble',
                'verbose_name': 'Tarifa del inmueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo_direccion', models.CharField(max_length=50, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['tipo_direccion'],
                'verbose_name_plural': 'Tipos de direccion',
                'verbose_name': 'Tipo de direccion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo_inmueble', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['tipo_inmueble'],
                'verbose_name_plural': 'Tipos de inmueble',
                'verbose_name': 'Tipo de inmueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('zona', models.CharField(max_length=100, unique=True)),
                ('ciudad', models.ForeignKey(to='direccion.Ciudad', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['ciudad', 'zona'],
                'verbose_name_plural': 'Zonas',
                'verbose_name': 'Zona',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='locaciones',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locaciones',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='pais', chained_model_field='pais', to='direccion.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locaciones',
            name='zona',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='ciudad', chained_model_field='ciudad', to='direccion.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inmueble',
            name='tarifa_valor',
            field=models.ForeignKey(to='direccion.Tarifa_valor', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inmueble',
            name='tipo_inmueble',
            field=models.ForeignKey(to='direccion.Tipo_Inmueble', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='pais', chained_model_field='pais', to='direccion.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='tipo_direccion',
            field=models.ForeignKey(to='direccion.Tipo_direccion', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='zona',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='ciudad', chained_model_field='ciudad', to='direccion.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(to='direccion.Provincia', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
