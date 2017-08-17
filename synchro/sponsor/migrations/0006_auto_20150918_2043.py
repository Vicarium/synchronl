# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_auto_20150911_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorpagesponsor',
            old_name='link_external',
            new_name='link',
        ),
        migrations.AddField(
            model_name='sponsorpagesponsor',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
