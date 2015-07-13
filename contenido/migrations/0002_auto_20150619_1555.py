# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20150619_1555'),
        ('servicio', '0002_auto_20150619_1555'),
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido_Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('predefinido', models.BooleanField(default=False)),
                ('contenido', models.ForeignKey(to='contenido.Contenido')),
                ('servicio', models.ForeignKey(to='servicio.Servicio')),
            ],
            options={
                'verbose_name_plural': 'Contenidos Servicios',
                'ordering': ['servicio', 'contenido'],
                'verbose_name': 'Contenido Servicio',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='contenido_servicio',
            unique_together=set([('contenido', 'servicio')]),
        ),
        migrations.RemoveField(
            model_name='contenido',
            name='contenedor',
        ),
        migrations.DeleteModel(
            name='Contenedor',
        ),
        migrations.AlterUniqueTogether(
            name='contenido_tipico',
            unique_together=set([('contenido', 'mueble')]),
        ),
    ]
