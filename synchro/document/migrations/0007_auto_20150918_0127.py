# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'documents', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock()))]),
        ),
    ]
