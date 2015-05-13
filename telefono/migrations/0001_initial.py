# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20150513_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Telefonos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tipo_telefono', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipos de telefonos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telefono',
            name='tipo_telefono',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='telefono.Tipo_telefono'),
            preserve_default=True,
        ),
    ]
