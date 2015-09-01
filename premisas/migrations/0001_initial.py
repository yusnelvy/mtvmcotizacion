# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=250)),
                ('telefonos', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('sitio_web', models.URLField()),
                ('correo', models.EmailField(max_length=254)),
                ('responsable', models.CharField(null=True, max_length=250, blank=True)),
                ('cuit', models.CharField(null=True, max_length=100, blank=True)),
                ('logo', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
