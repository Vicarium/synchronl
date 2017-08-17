# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150923_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='facebook_widget',
            field=models.TextField(blank=True),
        ),
    ]
