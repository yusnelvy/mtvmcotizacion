# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locaciones',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='locaciones',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='locaciones',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='locaciones',
            name='zona',
        ),
        migrations.DeleteModel(
            name='locaciones',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais', default=10, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zona',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais', default=10, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zona',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(to='direccion.Provincia', default=10, chained_field='pais', chained_model_field='pais'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(to='direccion.Provincia', chained_field='pais', chained_model_field='pais'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zona',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(to='direccion.Ciudad', chained_field='provincia', chained_model_field='provincia'),
            preserve_default=True,
        ),
    ]
