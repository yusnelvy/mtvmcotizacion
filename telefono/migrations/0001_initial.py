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
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('numero', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'ordering': ['numero'],
                'verbose_name_plural': 'Telefonos',
                'verbose_name': 'Telefono',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo_telefono', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['tipo_telefono'],
                'verbose_name_plural': 'Tipos de telefono',
                'verbose_name': 'Tipo de telefono',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telefono',
            name='tipo_telefono',
            field=models.ForeignKey(to='telefono.Tipo_telefono', default=1, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
