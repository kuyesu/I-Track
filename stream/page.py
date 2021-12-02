from django.db import models
from django.db.models.fields.related import ForeignKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from stream import blocks

# Create your models here.
class Dahboard(Page):
    template = "home/home_page.html"
    max_count = 1

    parent_page_type = [
        'wagtailcore.Page'
    ]

    page_title = models.CharField(max_length=45, null=True, blank=False)
    banner_subtitle = RichTextField(features=["bold", "italic", "link"],null=True, blank=False)
    banner_image = ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    child_detail = StreamField(
        [
            ("child_data", blocks.ChildDetails())
        ]
    )

    """Testing PAnels"""
    child_detail_panel = [
        MultiFieldPanel(
            [
                FieldPanel("page_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading = "Title options"
        ),
        StreamFieldPanel("child_detail")
    ]

    """tab"""

    edit_handler = TabbedInterface(
        [
            ObjectList(child_detail_panel , heading = "Child Details")
        ]
    )

    class Meta:
        verbose_name = "Home Page"
        verbose_name = "Home Pages"
        
        
    def get_admin_display_title(self):
        return "Dashboard"