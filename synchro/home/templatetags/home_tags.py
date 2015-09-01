# from datetime import date
# from django import template
# from django.conf import settings
#
# from blog.models import BlogPage
# from event.models import EventPage
# from wagtail.wagtailcore.models import Page
#
# register = template.Library()
#
#
# # Blog feed for home page
# @register.inclusion_tag(
#     'home/tags/blog_listing_homepage.html',
#     takes_context=True
# )
# def blog_listing_homepage(context, count=2):
#     blogs = BlogPage.objects.live().order_by('-date')
#     return {
#         'blogs': blogs[:count].select_related('feed_image'),
#         # required by the pageurl tag that we want to use within this template
#         'request': context['request'],
#     }
#
#
# # Events feed for home page
# @register.inclusion_tag(
#     'home/tags/event_listing_homepage.html',
#     takes_context=True
# )
# def event_listing_homepage(context, count=2):
#     events = EventPage.objects.live()
#     events = events.filter(date_from__gte=date.today()).order_by('date_from')
#     return {
#         'events': events[:count].select_related('feed_image'),
#         # required by the pageurl tag that we want to use within this template
#         'request': context['request'],
#     }
