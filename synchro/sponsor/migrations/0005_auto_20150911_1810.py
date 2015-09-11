# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0004_auto_20150905_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorpagesponsor',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
        ),
    ]
