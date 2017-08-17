# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20150908_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpage',
            name='name',
        ),
    ]
