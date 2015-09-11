# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0002_add_verbose_names'),
        ('common', '0003_auto_20150903_2323'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailsearch', '0002_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('blog', '0005_remove_extendedblogpage_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendedblogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='extendedblogpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='ExtendedBlogPage',
        ),
    ]
