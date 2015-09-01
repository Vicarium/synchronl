# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='intro',
            field=models.TextField(blank=True),
        ),
    ]
