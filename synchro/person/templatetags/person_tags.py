from django import template

from person.models import PersonPage, Page

register = template.Library()


# Person feed
@register.inclusion_tag(
    'person/tags/person_listing.html',
    takes_context=True
)
def person_listing(context, count=2):
    people = PersonPage.objects.live().order_by('?')
    return {
        'people': people[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
