# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre_principal', models.CharField(max_length=250)),
                ('dni', models.CharField(max_length=15, blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('comentarios', models.TextField(blank=True)),
                ('adicional1', models.CharField(max_length=50, blank=True)),
                ('adicional2', models.CharField(max_length=50, blank=True)),
                ('adicional3', models.CharField(max_length=50, blank=True)),
                ('adicional4', models.CharField(max_length=50, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre_principal'],
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('cliente', models.ForeignKey(default=1, to='cliente.Cliente')),
            ],
            options={
                'ordering': ['cliente', 'email'],
                'verbose_name_plural': 'Emails',
                'verbose_name': 'Email',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado_civil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado_civil', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['estado_civil'],
                'verbose_name_plural': 'Estados civil',
                'verbose_name': 'Estado civil',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sexo', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['sexo'],
                'verbose_name_plural': 'Sexos',
                'verbose_name': 'Sexo',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado_civil',
            field=models.ForeignKey(to='cliente.Estado_civil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.ForeignKey(to='cliente.Sexo'),
            preserve_default=True,
        ),
    ]
