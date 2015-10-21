# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('estado', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EstadoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('orden', models.IntegerField()),
                ('documento', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(to='gestiondocumento.Estado')),
            ],
            options={
                'verbose_name': 'Estado de documento',
                'verbose_name_plural': 'Estados de documentos',
                'ordering': ['estado', 'documento'],
            },
        ),
    ]
