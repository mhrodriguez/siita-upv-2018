# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 20:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestros',
            name='id_maestro',
        ),
        migrations.AlterField(
            model_name='maestros',
            name='num_empleado',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
