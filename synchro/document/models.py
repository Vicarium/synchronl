from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class DocumentPage(Page):
    documents = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('documents', blocks.ListBlock(blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('document', DocumentChooserBlock()),
        ])))
    ])

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

DocumentPage.content_panels = [
    StreamFieldPanel('body'),
]
