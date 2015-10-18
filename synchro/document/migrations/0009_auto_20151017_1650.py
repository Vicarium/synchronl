# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0003_add_verbose_names'),
        ('document', '0008_auto_20150918_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentPageSimpleDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('document', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='documentpagesimpledocument',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='simpledocument', to='document.DocumentPage'),
        ),
    ]
