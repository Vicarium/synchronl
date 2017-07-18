from django.db import models

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, \
    InlinePanel
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtaildocs.models import Document
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.fields import RichTextField

from modelcluster.fields import ParentalKey



# Abstract model for picking documents
class SimpleDocument(models.Model):
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        DocumentChooserPanel('document'),
    ]

    class Meta:
        abstract = True


class DocumentPage(Page):
    body = RichTextField(blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

DocumentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    InlinePanel('simpledocument', label="Documents")
]


class DocumentPageSimpleDocument(Orderable, SimpleDocument):
    page = ParentalKey('document.DocumentPage', related_name='simpledocument')
