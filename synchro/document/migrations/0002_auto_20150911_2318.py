# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentpage',
            old_name='documents',
            new_name='body',
        ),
    ]
