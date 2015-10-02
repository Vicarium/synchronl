from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailsearch import index


from modelcluster.fields import ParentalKey

from common.models import CarouselItem, RelatedLink

# Needs: body, newsfeed, upcoming events, advertising, sponsors, carousel
# Home Page

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='carousel_items')


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='related_links')


class HomePage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    twitter_widget = models.TextField(blank=True)
    facebook_widget = models.TextField(blank=True)
    small_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Homepage"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('body', classname="full"),
    FieldPanel('twitter_widget', classname="full"),
    FieldPanel('facebook_widget', classname="full"),
    ImageChooserPanel('small_image'),
    InlinePanel(HomePage, 'carousel_items', label="Carousel items"),
]

HomePage.promote_panels = Page.promote_panels
