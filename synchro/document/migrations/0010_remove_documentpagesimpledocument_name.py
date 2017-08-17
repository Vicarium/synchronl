# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_auto_20151017_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpagesimpledocument',
            name='name',
        ),
    ]
