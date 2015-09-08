from django.db import models

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.models import AbstractImage
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey


# Abstract model for picking images
class SimpleImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image')
    ]

    class Meta:
        abstract = True


# Basic Gallery page with optional thumbnail
class GalleryPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

GalleryPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('body', classname="full"),
    InlinePanel(GalleryPage, 'simpleimage', label="Images")
]

GalleryPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class GalleryPageSimpleImage(Orderable, SimpleImage):
    page = ParentalKey('gallery.GalleryPage', related_name='simpleimage')
