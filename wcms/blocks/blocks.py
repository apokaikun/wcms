"""Module providing custom base blocks."""

from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(StructBlock):
    """
    :HeadingBlock: Custom `StructBlock` that allows the user to select different header sizes.
    """

    heading_text = CharBlock(
        classname="title",
        require=True,
    )
    heading_size = ChoiceBlock(
        choices=[
            # ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class ImageBlock(StructBlock):
    """
    :ImageBlock: Custom `StructBlock` that allows users to select an image and optionally provide a title for it. This block is ideal for incorporating images with descriptive labels into page content.
    """

    image = ImageChooserBlock(require=True)
    caption = CharBlock(
        max_length=255,
        blank=True,
        required=False,
        help_text="Specify the title of the image.",
    )
    attribution = CharBlock(
        max_length=255,
        blank=True,
        required=False,
        help_text="Specify the attribution of the image.",
    )

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class QuoteBlock(StructBlock):
    """
    :QuoteBlock: Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribution = CharBlock(
        max_length=255, blank=True, required=False, label="e.g. John Doe."
    )

    class Meta:
        icon = "openquote"
        template = "blocks/qoute_block.html"


class HighlightsBlock(StructBlock):
    """
    :HighlightsBlock: Custom 'StructBlock that allows user to create highlights or summaries for the page.
    """

    format = ChoiceBlock(
        choices=[
            ("normal", "regular"),
            ("font-style : italic;", "italic"),
            ("font-weight: bold;", "bold"),
            ("font-style : italic; font-weight: bold;", "bold-italic"),
        ],
        blank=True,
        required=True,
    )
    highlight_items = ListBlock(
        CharBlock(max_length=512),
        blank=True,
        required=True,
    )

    class Meta:
        icon = "list"
        template = "blocks/highlight.html"


class MultiColumnBlock(StreamBlock):
    """
    :MultiColumnBlock: Custom `StreamBlock` that allows user to create multicolumn blocks.
    MultiColumnBlocks may contain the following:
    a. Paragraphs blocks
    b. Images blocks
    c. Quote blocks
    d. Embed (video, etc.)
    """

    paragraph_block = RichTextBlock()
    image_block = ImageBlock()
    block_quote = QuoteBlock()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL like a video from Youtube.",
    )

    class Meta:
        """
        Meta data to modify default Page attributes.
        """

        icon = "fa-columns"
        template = "blocks/multi_block.html"


class ReferenceBlock(StructBlock):
    """
    Custom Struckblock that allows user to create list of link urls.
    Useful when creating lists for Refences or Attributions.
    """

    reference = URLBlock()
    document = DocumentChooserBlock()

    class Meta:
        """
        Meta data to modify default Page attributes.
        """

        icon = "page"
        verbose_name = "Reference or Attibution"
        verbose_name_plural = "References or Attributions"


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    highlight_block = HighlightsBlock(icon="italic")
    paragraph_block = RichTextBlock()
    image_block = ImageBlock()
    block_quote = QuoteBlock()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL like a video from Youtube.",
    )
    two_column_block = MultiColumnBlock(max_num=2, min_num=2)
