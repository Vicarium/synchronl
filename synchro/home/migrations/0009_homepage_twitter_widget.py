# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='twitter_widget',
            field=models.TextField(blank=True),
        ),
    ]
