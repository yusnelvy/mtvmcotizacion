# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion_contenedor',
            name='contenedor',
        ),
        migrations.RemoveField(
            model_name='cotizacion_contenedor',
            name='cotizacion_mueble',
        ),
        migrations.AlterModelOptions(
            name='cotizacion_contenido',
            options={'verbose_name_plural': 'contenidos en el contenedor', 'ordering': ['cotizacion_mueble', 'contenido'], 'verbose_name': 'contenido en el contenedor'},
        ),
        migrations.AlterModelOptions(
            name='cotizacion_material',
            options={'verbose_name_plural': 'Materiales del mueble', 'ordering': ['cotizacion_servicio', 'material'], 'verbose_name': 'Material del mueble'},
        ),
        migrations.RemoveField(
            model_name='cotizacion_contenido',
            name='cotizacion_contenedor',
        ),
        migrations.DeleteModel(
            name='Cotizacion_Contenedor',
        ),
        migrations.AddField(
            model_name='cotizacion_contenido',
            name='cotizacion_mueble',
            field=models.ForeignKey(to='cotizacion.Cotizacion_Mueble', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_material',
            name='cotizacion_servicio',
            field=models.ForeignKey(to='cotizacion.Cotizacion_Servicio', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_mueble',
            name='densidad',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_mueble',
            name='peso',
            field=models.DecimalField(max_digits=5, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_servicio',
            name='cotizacion_contenido',
            field=models.ForeignKey(blank=True, default=1, to='cotizacion.Cotizacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion_servicio',
            name='tipo',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='ocupacion',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cotizacion_material',
            unique_together=set([('cotizacion_servicio', 'material')]),
        ),
        migrations.RemoveField(
            model_name='cotizacion_material',
            name='cotizacion_mueble',
        ),
    ]
