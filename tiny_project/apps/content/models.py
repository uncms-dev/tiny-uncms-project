from cms.apps.pages.models import ContentBase
from cms.models import HtmlField
from django.db import models


class Content(ContentBase):
    # We can define no fields at all here! Just its existence as a
    # non-abstract class inheriting from ContentBase will make it available
    # in the page types.
    #
    # We don't have to specify a urlconf as we did in the news app. If you
    # don't specify one, it will default to rendering the template at
    # `<app_label>/<modelname>.html` - i.e. `content/content.html` in this case.
    pass


class ContentSection(models.Model):
    # This is a model which will be registered inline so that you can edit it
    # directly from the page's admin screen.
    #
    # This ForeignKey to `pages.Page` is entirely necessary in order to make
    # inlines work. Note that it is to the *Page* itself and not the content
    # model!
    page = models.ForeignKey(
        'pages.Page',
    )

    title = models.CharField(
        max_length=100,
    )

    # HtmlField is explained in more depth over in the news app.
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
