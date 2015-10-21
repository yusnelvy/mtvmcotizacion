# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondocumento', '0001_initial'),
        ('presupuesto', '0040_auto_20151013_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('estado', models.ForeignKey(to='gestiondocumento.EstadoDocumento')),
            ],
            options={
                'verbose_name': 'Estado del presupuesto',
                'verbose_name_plural': 'Estados del presupuesto',
            },
        ),
        migrations.RemoveField(
            model_name='presupuesto',
            name='activo',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='comentario_activo',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='presupuestoestado',
            name='presupuesto',
            field=models.ForeignKey(to='presupuesto.Presupuesto'),
        ),
    ]
