# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 02:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_auto_20191015_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 2, 4, 37, 594166), verbose_name='Start'),
        ),
    ]
