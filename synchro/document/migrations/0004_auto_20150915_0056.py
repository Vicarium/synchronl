# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20150915_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
    ]
