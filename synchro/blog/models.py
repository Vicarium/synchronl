from datetime import date

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index

from common.models import CarouselItem, RelatedLink, LinkFields

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase


# Individual Blog Page


class BlogPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey(
        "blog.BlogPage", on_delete=models.CASCADE, related_name="carousel_items"
    )


class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        "blog.BlogPage", on_delete=models.CASCADE, related_name="related_links"
    )


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "blog.BlogPage", on_delete=models.CASCADE, related_name="tagged_items"
    )


class BlogPage(Page):
    body = RichTextField()
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")
    parent_page_types = ["blog.BlogIndexPage"]
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = Page.search_fields + [index.SearchField("body")]

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()


BlogPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("date"),
    FieldPanel("body", classname="full"),
    InlinePanel("carousel_items", label="Carousel items"),
]

BlogPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel("feed_image"),
    FieldPanel("tags"),
]


# Blog index page


class BlogIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        "blog.BlogIndexPage", on_delete=models.CASCADE, related_name="related_links"
    )


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ["blog.BlogPage"]

    search_fields = Page.search_fields + [index.SearchField("intro")]

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by("-date")

        return blogs

    def get_context(self, request):
        # Get blogs
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get("tag")
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(blogs, 10)  # Show 10 blogs per page
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context["blogs"] = blogs
        return context


BlogIndexPage.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel("intro", classname="full"),
]

BlogIndexPage.promote_panels = Page.promote_panels


# Related links


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [FieldPanel("title"), MultiFieldPanel(LinkFields.panels, "Link")]

    class Meta:
        abstract = True
