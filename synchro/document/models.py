from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsearch import index



class DocumentPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('documents', blocks.ListBlock(DocumentChooserBlock()))
    ])

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

DocumentPage.content_panels = [
    StreamFieldPanel('body'),
]
