# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150903_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
    ]
