# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20150515_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ambiente', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ambiente_Tipo_inmueble',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('tipo_inmueble', models.ForeignKey(to='direccion.Tipo_Inmueble')),
            ],
            options={
                'verbose_name': 'Ambiente - Tipo inmueble',
                'verbose_name_plural': 'Ambientes - Tipos de inmueble',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_ambiente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tipo_ambiente', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de ambiente',
                'verbose_name_plural': 'Tipos de ambiente',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='tipo_ambiente',
            field=models.ForeignKey(to='ambiente.Tipo_ambiente'),
            preserve_default=True,
        ),
    ]
