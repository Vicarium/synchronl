# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_auto_20150904_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorpagesponsor',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', null=True),
        ),
    ]
