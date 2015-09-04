# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('text', models.CharField(max_length=255)),
                ('page', models.ForeignKey(related_name='adverts', blank=True, to='wagtailcore.Page', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertPlacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advert', models.ForeignKey(related_name='+', to='common.Advert')),
                ('page', modelcluster.fields.ParentalKey(related_name='advert_placements', to='wagtailcore.Page')),
            ],
        ),
    ]
