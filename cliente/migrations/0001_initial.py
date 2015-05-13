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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre_principal', models.CharField(max_length=250)),
                ('comentarios', models.TextField(blank=True)),
                ('adicional1', models.CharField(blank=True, max_length=50)),
                ('adicional2', models.CharField(blank=True, max_length=50)),
                ('adicional3', models.CharField(blank=True, max_length=50)),
                ('adicional4', models.CharField(blank=True, max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('cliente', models.ForeignKey(default=1, to='cliente.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
