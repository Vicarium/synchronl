from __future__ import unicode_literals

from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index


from modelcluster.fields import ParentalKey


class TeamPage(Page):
    intro = models.TextField(blank=True)
    announcements = RichTextField(blank=True)
    schedule = RichTextField(blank=True)
    roster = RichTextField(blank=True)
    team_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('schedule'),
        index.SearchField('announcements'),
        index.SearchField('roster'),
    ]

TeamPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('schedule', classname="full"),
    FieldPanel('announcements', classname="full"),
    FieldPanel('roster', classname="full"),
    ImageChooserPanel('team_photo'),
]

TeamPage.promote_panels = Page.promote_panels
