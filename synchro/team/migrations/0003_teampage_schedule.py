# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_teampage_announcements'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='schedule',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
