# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-16 20:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0002_auto_20180415_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999999)]),
        ),
    ]
