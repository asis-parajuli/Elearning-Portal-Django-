# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-05 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20190405_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(choices=[('1', 'List of things to do'), ('2', 'Works Inprogress'), ('3', 'Works completed')], max_length=50),
        ),
    ]