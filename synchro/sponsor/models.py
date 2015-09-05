from django.db import models

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image

from modelcluster.fields import ParentalKey


# Abstract model for sponsors
class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    link_external = models.URLField("External link", blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('link_external'),
        ImageChooserPanel('image')
    ]

    class Meta:
        abstract = True


# Page for listing sponsors/partners
class SponsorPage(Page):
    intro = models.TextField(blank=True)

SponsorPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel(SponsorPage, 'sponsor', label="Sponsors"),
]


class SponsorPageSponsor(Orderable, Sponsor):
    page = ParentalKey('sponsor.SponsorPage', related_name='sponsor')
