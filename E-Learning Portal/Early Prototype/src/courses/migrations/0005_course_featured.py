# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190314_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
