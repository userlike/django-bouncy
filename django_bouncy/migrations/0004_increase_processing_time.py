# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-02 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bouncy', '0003_auto_20151106_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='processing_time',
            field=models.IntegerField(default=0),
        ),
    ]