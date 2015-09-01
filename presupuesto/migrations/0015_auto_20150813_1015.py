# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0014_auto_20150810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosprecargado',
            name='altomueble',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='anchomueble',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='cappesocontenedormueble',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='densidadcontenidomueble',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='factorcomplejidadinmueble',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='factortiempocompservicio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='largomueble',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='montomaterial',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='peso_contenedormueble',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='pesomaterial',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='pesomueble',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='preciomaterial',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='tarifacomplejidadservicio',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='valorambcompleinmueble',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='valorm3compleinmueble',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='datosprecargado',
            name='valorocupacioninmueble',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_con_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_materiales',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_persona',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_servicios',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_sin_impuesto',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_vehiculo_hora',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='monto_vehiculo_recorrido',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_carga',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_recorrido',
            field=models.DecimalField(decimal_places=2, max_digits=7, default=1.0, choices=[(1.0, 'Entre 30 minuto a 1 hora'), (2.0, 'Entre 1 hora a 2 horas'), (3.0, 'Entre 2 horas a 3 horas'), (4.0, 'Entre 3 horas a 4 horas'), (5.0, 'Entre 4 horas a 5 horas'), (6.0, 'Entre 5 horas a 6 horas'), (7.0, 'Entre 6 horas a 7 horas'), (8.0, 'Entre 7 horas a 8 horas'), (9.0, 'Entre 8 horas a 9 horas'), (10.0, 'Más de 10 horas')]),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_servicios',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tiempo_total',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_contenedores',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_contenidos',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_materiales',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_mudanza',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='total_peso_muebles',
            field=models.DecimalField(decimal_places=3, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='alto',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='ancho',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='capacidad_peso_contenedor',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='largo',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso_contenedor',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='peso_contenido',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_detalle',
            name='valor_densidad',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='factor_complejidad',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='total_m2',
            field=models.DecimalField(decimal_places=2, max_digits=7, default=0, choices=[(40, 'Entre 40 metros cuadrado'), (80, 'Entre 41 a 80 metros cuadrado'), (120, 'Entre 81 a 120 metros cuadrado'), (160, 'Entre 121 a 160 metros cuadrado'), (200, 'Entre 161 a 200 metros cuadrado'), (200, 'Mas de 200 metros cuadrado')]),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='valor_ambiente_complejidad',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_direccion',
            name='valor_metrocubico_complejiadad',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='monto_material',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='monto_servicio',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='peso_material',
            field=models.DecimalField(decimal_places=3, blank=True, default='0.000', max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='precio_material',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=9),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='tiempo_aplicado',
            field=models.DecimalField(decimal_places=2, blank=True, default='0.00', max_digits=7),
        ),
        migrations.AlterField(
            model_name='presupuesto_servicio',
            name='volumen_material',
            field=models.DecimalField(decimal_places=3, blank=True, default='0.000', max_digits=8),
        ),
    ]
