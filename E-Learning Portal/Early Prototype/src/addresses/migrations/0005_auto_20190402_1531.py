# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_auto_20190324_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
