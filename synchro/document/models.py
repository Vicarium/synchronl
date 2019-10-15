from django.db import models

from wagtail.core.models import Orderable, Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.models import Document
from wagtail.search import index
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey


# Abstract model for picking documents
class SimpleDocument(models.Model):
    document = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [DocumentChooserPanel("document")]

    class Meta:
        abstract = True


class DocumentPage(Page):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [index.SearchField("body")]


DocumentPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("body", classname="full"),
    InlinePanel("simpledocument", label="Documents"),
]


class DocumentPageSimpleDocument(Orderable, SimpleDocument):
    page = ParentalKey(
        "document.DocumentPage", on_delete=models.CASCADE, related_name="simpledocument"
    )
