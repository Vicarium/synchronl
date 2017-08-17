# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(max_length=255, choices=[('public', 'Public'), ('private', 'Private')]),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_to',
            field=models.DateField(help_text='Not required if event is on a single day', blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_from',
            field=models.TimeField(blank=True, null=True, verbose_name='Start time'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(blank=True, verbose_name='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(blank=True, verbose_name='Surname', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
    ]
