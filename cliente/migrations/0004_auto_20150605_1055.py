# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20150515_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_civil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('estado_civil', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'verbose_name': 'Estado civil',
                'verbose_name_plural': 'Estados civil',
                'ordering': ['estado_civil'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sexo', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
                'ordering': ['sexo'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes', 'ordering': ['nombre_principal']},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails', 'ordering': ['cliente', 'email']},
        ),
        migrations.AddField(
            model_name='cliente',
            name='dni',
            field=models.CharField(blank=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default='2001-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
