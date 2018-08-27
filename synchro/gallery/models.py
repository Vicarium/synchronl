from django.db import models

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.models import AbstractImage
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


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


class GalleryPageTag(TaggedItemBase):
    content_object = ParentalKey('GalleryPage', related_name='tagged_items')


# Basic Gallery page with optional thumbnail
class GalleryPage(Page):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_tags = ClusterTaggableManager(through=GalleryPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]


    def get_images(self):
        """ Get images with tag or manually added to gallery and return them sorted by creation date """

        id_list = []
        for simple_image in self.simpleimage.all():
            id_list.append(simple_image.image.id)
        manual_set = Image.objects.filter(id__in=id_list)

        tag_set = Image.objects.none()
        for tag in self.image_tags.all():
            tag_set = tag_set.union(Image.objects.all().filter(tags__name=tag.name))

        union_set = tag_set.union(manual_set)

        return union_set.order_by('-created_at')


GalleryPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    FieldPanel('image_tags', classname="full"),
    InlinePanel('simpleimage', label="Images")
]

GalleryPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class GalleryPageSimpleImage(Orderable, SimpleImage):
    page = ParentalKey('gallery.GalleryPage', related_name='simpleimage')
