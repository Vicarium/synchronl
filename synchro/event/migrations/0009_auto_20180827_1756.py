# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-27 17:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20170829_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 17, 56, 13, 858708), verbose_name='Start'),
        ),
    ]
