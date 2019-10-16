from cms.apps.pages.models import ContentBase
from cms.models import HtmlField
from django.db import models


class Content(ContentBase):
    # We can define no fields at all here! Just its existence as a
    # non-abstract class inheriting from ContentBase will make it available
    # in the page types.
    pass


class ContentSection(models.Model):
    title = models.CharField(
        max_length=100,
    )

    text = HtmlField(
        null=True,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
