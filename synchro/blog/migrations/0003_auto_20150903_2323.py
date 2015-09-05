# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150901_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
    ]
