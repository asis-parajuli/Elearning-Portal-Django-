# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-06 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0004_auto_20190405_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
        ),
    ]
