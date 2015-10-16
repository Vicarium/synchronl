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
def blog_listing(context, count=4):
    site_root = context['request'].site.root_page
    blogs = BlogPage.objects.descendant_of(site_root).live()
    blogs = blogs.order_by('-date')
    return {
        'blogs': blogs[1:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Blog feed for sidebar on other pages
@register.inclusion_tag(
    'blog/tags/blog_simple_listing.html',
    takes_context=True
)
def blog_simple_listing(context, count=5):
    site_root = context['request'].site.root_page
    blogs = BlogPage.objects.descendant_of(site_root).live()
    blogs = blogs.order_by('-date')
    return {
        'blogs': blogs[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Featured blog post for front page
@register.inclusion_tag(
    'blog/tags/blog_feature.html',
    takes_context=True
)
def blog_feature(context, count=1):
    site_root = context['request'].site.root_page
    blogs = BlogPage.objects.descendant_of(site_root).live()
    blogs = blogs.order_by('-date')
    return {
        'blogs': blogs[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
