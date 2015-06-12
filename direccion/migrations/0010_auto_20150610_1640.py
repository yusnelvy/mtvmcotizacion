# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0009_inmueble_tarifa_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='locaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_model_field='provincia', chained_field='provincia', to='direccion.Ciudad')),
                ('pais', models.ForeignKey(to='direccion.Pais')),
                ('provincia', smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', chained_field='pais', to='direccion.Provincia')),
                ('zona', smart_selects.db_fields.ChainedForeignKey(chained_model_field='ciudad', chained_field='ciudad', to='direccion.Zona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='direccion',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(default=1, chained_field='provincia', to='direccion.Ciudad', chained_model_field='provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='pais',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='direccion.Pais'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(default=2, chained_field='pais', to='direccion.Provincia', chained_model_field='pais'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='zona',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='ciudad', chained_field='ciudad', to='direccion.Zona'),
            preserve_default=True,
        ),
    ]
