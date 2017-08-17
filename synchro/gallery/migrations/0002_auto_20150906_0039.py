# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='sponsorpagesponsor',
            name='page',
        ),
        migrations.RemoveField(
            model_name='sponsorpagesponsor',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='sponsorpagesponsor',
            name='uploaded_by_user',
        ),
        migrations.CreateModel(
            name='GalleryPageSimpleImage',
            fields=[
                ('simpleimage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gallery.SimpleImage')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='galleryimage', to='gallery.GalleryPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('gallery.simpleimage', models.Model),
        ),
        migrations.DeleteModel(
            name='SponsorPageSponsor',
        ),
        migrations.AddField(
            model_name='simpleimage',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', null=True),
        ),
    ]
