# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150906_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerypagesimpleimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='gallerypagesimpleimage',
            name='simpleimage_ptr',
        ),
        migrations.RemoveField(
            model_name='simpleimage',
            name='image',
        ),
        migrations.DeleteModel(
            name='GalleryPageSimpleImage',
        ),
        migrations.DeleteModel(
            name='SimpleImage',
        ),
    ]
