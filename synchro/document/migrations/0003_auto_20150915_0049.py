# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20150911_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'documents', wagtail.core.blocks.StructBlock([(b'name', wagtail.core.blocks.CharBlock(required=True)), (b'document', wagtail.documents.blocks.DocumentChooserBlock())]))]),
        ),
    ]
