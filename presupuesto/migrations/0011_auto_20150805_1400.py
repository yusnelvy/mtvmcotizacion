# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0010_presupuesto_activo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto_servicio',
            old_name='tarifa',
            new_name='cantidad_material',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_materiales',
            field=models.DecimalField(blank=True, default=0.0, max_digits=7, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='monto_servicios',
            field=models.DecimalField(blank=True, default=0.0, max_digits=7, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='tiempo_servicios',
            field=models.DecimalField(blank=True, default='0.00', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto_servicio',
            name='monto_servicio',
            field=models.DecimalField(blank=True, default='0.00', max_digits=7, decimal_places=2),
        ),
        migrations.AddField(
            model_name='presupuesto_servicio',
            name='precio_material',
            field=models.DecimalField(blank=True, default='0.00', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_capacidad_vehiculo',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_m3',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_contenedores',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_contenidos',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_materiales',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_mudanza',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_muebles',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_volumen_contenedores',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_volumen_contenidos',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_volumen_materiales',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_volumen_muebles',
            field=models.DecimalField(blank=True, default=0.0, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='capacidad_peso_contenedor',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='capacidad_volumen_contenedor',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso_contenedor',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso_contenido',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='valor_ocupacidad',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='volumen_contenedor',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='volumen_contenido',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='volumen_mueble',
            field=models.DecimalField(max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='factor_complejidad',
            field=models.DecimalField(blank=True, default=0.0, max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='valor_ambiente_complejidad',
            field=models.DecimalField(blank=True, default=0.0, max_digits=13, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='valor_metrocubico_complejiadad',
            field=models.DecimalField(blank=True, default=0.0, max_digits=13, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='valor_ocupacidad',
            field=models.DecimalField(blank=True, default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='peso_material',
            field=models.DecimalField(blank=True, default='0.00', max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='volumen_material',
            field=models.DecimalField(blank=True, default='0.00', max_digits=8, decimal_places=3),
        ),
    ]
