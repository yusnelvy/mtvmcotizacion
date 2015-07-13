# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('unidad', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Unidads',
                'ordering': ['unidad'],
                'verbose_name': 'Unidad',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name_plural': 'Servicios', 'ordering': ['servicio'], 'verbose_name': 'Servicio'},
        ),
        migrations.AddField(
            model_name='material',
            name='alto',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='ancho',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='capacidad_peso',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='capacidad_volumen',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='contenedor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material',
            name='largo',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='volumen',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='complejidad_servicio',
            unique_together=set([('servicio', 'complejidad')]),
        ),
        migrations.AlterUniqueTogether(
            name='servicio_material',
            unique_together=set([('servicio', 'material')]),
        ),
    ]
