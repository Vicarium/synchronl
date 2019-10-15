from datetime import date, datetime, timedelta

from django.db import models
from django.http import HttpResponse

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey

from common.models import RelatedLink, CarouselItem, LinkFields

from event.utils import export_event


EVENT_AUDIENCE_CHOICES = (("public", "Public"), ("private", "Private"))


EVENT_TYPE_CHOICES = (
    ("other", "Other"),
    ("camp", "Camp"),
    ("celebration", "Celebration"),
    ("competition", "Competition"),
    ("fundraiser", "Fundraiser"),
    ("meeting", "Meeting"),
)

# Generate a start date for datetime fields
def default_start_date():
    now = datetime.today()
    start = now + timedelta(days=1)
    return start


# Event index page
class EventIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        "event.EventIndexPage", on_delete=models.CASCADE, related_name="related_links"
    )


class EventIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ["event.EventPage"]

    search_fields = Page.search_fields + [index.SearchField("intro")]

    @property
    def events(self):
        # Get list of live event pages that are descendants of this page
        events = EventPage.objects.live().descendant_of(self)

        # Filter events list to get ones that are either
        # running now or start in the future
        events = events.filter(date_from__gte=date.today())

        # Order by date
        events = events.order_by("date_from")

        return events


EventIndexPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
]

EventIndexPage.promote_panels = Page.promote_panels


# Event page


class EventPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey(
        "event.EventPage", on_delete=models.CASCADE, related_name="carousel_items"
    )


class EventPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        "event.EventPage", on_delete=models.CASCADE, related_name="related_links"
    )


class EventPageSpeaker(Orderable, LinkFields):
    page = ParentalKey(
        "event.EventPage", on_delete=models.CASCADE, related_name="speakers"
    )
    first_name = models.CharField("Name", max_length=255, blank=True)
    last_name = models.CharField("Surname", max_length=255, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    @property
    def name_display(self):
        return self.first_name + " " + self.last_name

    panels = [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        ImageChooserPanel("image"),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]


class EventPage(Page):
    date_from = models.DateTimeField(
        "Start", null=False, blank=False, default=default_start_date()
    )
    date_to = models.DateTimeField("End", null=True, blank=True)
    audience = models.CharField(max_length=255, choices=EVENT_AUDIENCE_CHOICES)
    location = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    cost = models.CharField(max_length=255)
    event_type = models.CharField(
        max_length=32, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_CHOICES[0]
    )
    signup_link = models.URLField(blank=True)
    parent_page_types = ["event.EventIndexPage"]
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = Page.search_fields + [
        index.SearchField("get_audience_display"),
        index.SearchField("location"),
        index.SearchField("body"),
    ]

    @property
    def event_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(EventIndexPage).last()

    def get_color(self):

        color_choices = {
            "other": "sandybrown",
            "camp": "goldenrod",
            "celebration": "limegreen",
            "competition": "blue",
            "fundraiser": "aqua",
            "meeting": "purple",
        }

        return color_choices[self.event_type]

    def serve(self, request):
        if "format" in request.GET:
            if request.GET["format"] == "ical":
                # Export to ical format
                response = HttpResponse(
                    export_event(self, "ical"), content_type="text/calendar"
                )
                response["Content-Disposition"] = (
                    "attachment; filename=" + self.slug + ".ics"
                )
                return response
            else:
                # Unrecognised format error
                message = (
                    "Could not export event\n\nUnrecognised format: "
                    + request.GET["format"]
                )
                return HttpResponse(message, content_type="text/plain")
        else:
            # Display event page as usual
            return super(EventPage, self).serve(request)


EventPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("date_from"),
    FieldPanel("date_to"),
    FieldPanel("location"),
    FieldPanel("event_type"),
    FieldPanel("audience"),
    FieldPanel("cost"),
    FieldPanel("signup_link"),
    InlinePanel("carousel_items", label="Carousel items"),
    FieldPanel("body", classname="full"),
    InlinePanel("speakers", label="Speakers"),
]

EventPage.promote_panels = Page.promote_panels + [ImageChooserPanel("feed_image")]
