# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20150903_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personpage',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='last_name',
        ),
    ]
