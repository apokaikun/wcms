"""Module providing base models."""

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.search.index import SearchField

from wcms.blocks import BaseStreamBlock
from wagtail.snippets.models import register_snippet

class StandardPage(Page):
    """
    Generic page that can be use as a base for other custom pages.
    """

    introduction = models.TextField(
        help_text="Text to describe the page",
        blank=True,
        verbose_name="Introduction or Summary",
    )

    body = StreamField(
        BaseStreamBlock(),
    )

    # Image is used in this context as the banner image for this page.
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
        verbose_name="hero image",
    )

    # Feature image is used in this context as the image this page is
    # linked/referenced in other pages.
    feature_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
        verbose_name="feature image",
    )

    # Add custom fields' panels to Page's defaul content panels.
    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("feature_image"),
    ]

    # Define the search fields for this page.
    search_fields = Page.search_fields + [
        SearchField("title", partial_match=True),
        SearchField("introduction", partial_match=True),
        SearchField("body", partial_match=True),
    ]


# Start of snippet section.
# Snippets Sections: Allows Administrator to set standard Header and Footer.
@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """

    body = RichTextField()

    panels = [
        FieldPanel("body"),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = "Footer Text"


@register_snippet
class HeaderText(models.Model):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
        verbose_name="hero image",
    )

    panels = [FieldPanel("image")]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = "Header Text"


# End of snippets section.
