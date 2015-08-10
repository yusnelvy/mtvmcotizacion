# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0009_auto_20150805_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Ambiente'),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='cotizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion'),
        ),
        migrations.AlterField(
            model_name='cotizacion_ambiente',
            name='piso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Piso'),
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='contenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenido.Contenido'),
        ),
        migrations.AlterField(
            model_name='cotizacion_contenido',
            name='cotizacion_mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion_Mueble'),
        ),
        migrations.AlterField(
            model_name='cotizacion_direccion',
            name='cotizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion'),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='cotizacion_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion_Servicio'),
        ),
        migrations.AlterField(
            model_name='cotizacion_material',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Material'),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='cotizacion_ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion_Ambiente'),
        ),
        migrations.AlterField(
            model_name='cotizacion_mueble',
            name='mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Mueble'),
        ),
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='cotizacion_mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion_Mueble'),
        ),
        migrations.AlterField(
            model_name='cotizacion_servicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicio.Servicio'),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trabajador.Cargo_trabajador'),
        ),
        migrations.AlterField(
            model_name='cotizacion_trabajador',
            name='cotizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion'),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='cotizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Cotizacion'),
        ),
        migrations.AlterField(
            model_name='vehiculo_cotizacion',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Vehiculo'),
        ),
    ]
