from django.db import models

from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

from modelcluster.fields import ParentalKey


# Abstract model for sponsors
class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    link = models.URLField("External link", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name", classname="full"),
        FieldPanel("text", classname="full"),
        FieldPanel("link", classname="full"),
        ImageChooserPanel("image"),
    ]

    class Meta:
        abstract = True


# Page for listing sponsors/partners
class SponsorPage(Page):
    intro = models.TextField(blank=True)


SponsorPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
    InlinePanel("sponsor", label="Sponsors"),
]


class SponsorPageSponsor(Orderable, Sponsor):
    page = ParentalKey(
        "sponsor.SponsorPage", on_delete=models.CASCADE, related_name="sponsor"
    )
