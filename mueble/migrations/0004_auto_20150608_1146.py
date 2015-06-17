# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0003_auto_20150604_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Densidad',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Densidad',
                'verbose_name_plural': 'Densidades',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='tamano',
            name='descripcion',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Mueble'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamano_mueble',
            name='tamano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Tamano'),
            preserve_default=True,
        ),
    ]
