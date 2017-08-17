# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_twitter_widget'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='logo',
            new_name='small_image',
        ),
    ]
