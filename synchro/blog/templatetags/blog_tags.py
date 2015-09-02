from datetime import date
from django import template
from django.conf import settings

from blog.models import BlogPage
from wagtail.wagtailcore.models import Page

register = template.Library()


# Blog feed for home page
@register.inclusion_tag(
    'blog/tags/blog_listing.html',
    takes_context=True
)
def blog_listing(context, count=2):
    blogs = BlogPage.objects.live().order_by('-date')
    return {
        'blogs': blogs[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }