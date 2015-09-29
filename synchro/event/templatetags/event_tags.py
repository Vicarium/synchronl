from datetime import date
from django import template
from django.conf import settings

from event.models import EventPage
from wagtail.wagtailcore.models import Page

register = template.Library()


# Events feed for home page
@register.inclusion_tag(
    'event/tags/event_listing.html',
    takes_context=True
)
def event_listing(context, count=5):
    events = EventPage.objects.live()
    events = events.filter(date_from__gte=date.today()).order_by('date_from')
    return {
        'events': events[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
