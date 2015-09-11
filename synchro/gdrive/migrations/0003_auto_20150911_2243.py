# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdrive', '0002_auto_20150910_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gdrivepage',
            old_name='folder_id',
            new_name='link',
        ),
    ]
