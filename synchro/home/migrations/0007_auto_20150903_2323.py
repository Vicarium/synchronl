# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150901_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
    ]
