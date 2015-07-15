# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dni', models.CharField(max_length=20)),
                ('nombre_cliente', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_estimadamudanza', models.DateTimeField()),
                ('descripcion_vehiculo', models.TextField()),
                ('descripcion_persona', models.TextField()),
                ('cantidad_vehiculo', models.IntegerField(default=0, blank=True)),
                ('cantidad_persona', models.IntegerField(default=0, blank=True)),
                ('cantidad_ambientes', models.IntegerField(default=0, blank=True)),
                ('cantidad_muebles', models.IntegerField(default=0, blank=True)),
                ('cantidad_contenedores', models.IntegerField(default=0, blank=True)),
                ('total_peso_contenedores', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('total_peso_muebles', models.DecimalField(max_digits=5, default=0.0, decimal_places=2, blank=True)),
                ('total_peso_contenidos', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('total_volumen_muebles', models.DecimalField(max_digits=5, default=0.0, decimal_places=2, blank=True)),
                ('total_volumen_contenedores', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('total_volumen_contenidos', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('total_m3', models.DecimalField(max_digits=7, decimal_places=2)),
                ('recorrido_km', models.DecimalField(max_digits=7, decimal_places=2)),
                ('tiempo_recorrido', models.TimeField()),
                ('tiempo_carga', models.TimeField()),
                ('tiempo_total', models.TimeField()),
                ('monto_vehiculo_hora', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('monto_vehiculo_recorrido', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('monto_persona', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('monto_sin_impuesto', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('monto_impuesto', models.DecimalField(max_digits=7, default=0.0, decimal_places=2, blank=True)),
                ('monto_con_impuesto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('cotizador', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='creado_por')),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuestos',
            },
        ),
        migrations.CreateModel(
            name='Presupuesto_Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ambiente', models.CharField(max_length=100)),
                ('mueble', models.CharField(max_length=100)),
                ('tamano', models.CharField(max_length=100)),
                ('ancho', models.DecimalField(max_digits=5, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=5, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=5, decimal_places=2)),
                ('densidad', models.CharField(max_length=100)),
                ('valor_densidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ocupacidad', models.CharField(max_length=100)),
                ('valor_ocupacidad', models.DecimalField(max_digits=3, decimal_places=2)),
                ('cantidad_contenedor', models.IntegerField()),
                ('volumen_contenido', models.DecimalField(max_digits=7, decimal_places=2)),
                ('volumen_contenedor', models.DecimalField(max_digits=7, decimal_places=2)),
                ('volumen_mueble', models.DecimalField(max_digits=7, decimal_places=2)),
                ('capacidad_peso_contenedor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('capacidad_volumen_contenedor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('peso_contenido', models.DecimalField(max_digits=7, decimal_places=2)),
                ('peso_contenedor', models.DecimalField(max_digits=7, decimal_places=2)),
                ('presupuesto', models.ForeignKey(to='presupuesto.Presupuesto')),
            ],
            options={
                'verbose_name': 'detalle del presupuesto',
                'verbose_name_plural': 'detalle del presupuesto',
                'ordering': ['presupuesto', 'ambiente', 'mueble'],
            },
        ),
        migrations.CreateModel(
            name='Presupuesto_direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('direccion', models.TextField()),
                ('tipo_direccion', models.CharField(max_length=100)),
                ('inmueble', models.CharField(max_length=100)),
                ('tipo_inmueble', models.CharField(max_length=100)),
                ('ocupacidad_inmueble', models.CharField(max_length=100)),
                ('valor_ocupacidad', models.DecimalField(max_digits=3, decimal_places=2)),
                ('pisos', models.IntegerField()),
                ('pisos_escalera', models.IntegerField()),
                ('rampa', models.BooleanField()),
                ('ascensor', models.BooleanField()),
                ('ascensor_servicio', models.BooleanField()),
                ('pisos_ascensor_servicio', models.IntegerField()),
                ('pisos_ascensor', models.IntegerField()),
                ('complejidad', models.CharField(max_length=100)),
                ('factor_complejidad', models.DecimalField(max_digits=4, decimal_places=2)),
                ('valor_ambiente_complejidad', models.DecimalField(max_digits=13, decimal_places=2)),
                ('valor_metrocubico_complejiadad', models.DecimalField(max_digits=13, decimal_places=2)),
                ('distancia_vehiculo', models.IntegerField()),
                ('total_m2', models.DecimalField(max_digits=5, decimal_places=2)),
                ('presupuesto', models.ForeignKey(to='presupuesto.Presupuesto')),
            ],
            options={
                'verbose_name': 'direccion del presupuesto',
                'verbose_name_plural': 'direcciones del presupuesto',
                'ordering': ['presupuesto', 'direccion'],
            },
        ),
    ]
