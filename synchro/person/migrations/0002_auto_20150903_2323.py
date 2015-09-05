# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
    ]
