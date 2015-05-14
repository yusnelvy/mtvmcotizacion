# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Provincia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='tipo_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Tipo_direccion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Zona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='complejidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Complejidad_Inmueble'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Direccion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='tipo_inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Tipo_Inmueble'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zona',
            name='cuidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Ciudad'),
            preserve_default=True,
        ),
    ]
