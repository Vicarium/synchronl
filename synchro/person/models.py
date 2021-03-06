from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey

from common.models import RelatedLink, StandardIndexPage


# Contact info


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel("telephone"),
        FieldPanel("email"),
        FieldPanel("address_1"),
        FieldPanel("address_2"),
        FieldPanel("city"),
        FieldPanel("country"),
        FieldPanel("post_code"),
    ]

    class Meta:
        abstract = True


# Person page


class PersonPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        "person.PersonPage", on_delete=models.CASCADE, related_name="related_links"
    )


class PersonPage(Page, ContactFields):
    intro = RichTextField(blank=True)
    biography = RichTextField(blank=True)
    parent_page_types = ["common.StandardIndexPage"]

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = Page.search_fields + [
        index.SearchField("title"),
        index.SearchField("intro"),
        index.SearchField("biography"),
    ]


PersonPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
    FieldPanel("biography", classname="full"),
    ImageChooserPanel("image"),
    MultiFieldPanel(ContactFields.panels, "Contact"),
]

PersonPage.promote_panels = Page.promote_panels + [ImageChooserPanel("feed_image")]
