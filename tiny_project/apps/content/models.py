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

    def get_searchable_text(self):
        # If you use Watson for your search on your frontend (you really
        # should, it rules), then by default the Page model will be registered
        # with it. The search adapter for the Page model will smoosh together
        # all of the text fields (CharField and TextField) into the blob of
        # text that Watson searches with a low weighting.
        #
        # That works fine, but in our case all of our page's textual content
        # is in ContentSection objects. To make Watson see this text, we
        # just need to override get_searchable_text on our content model and
        # throw in all of the text of our ContentSection too.
        text = super().get_searchable_text()
        return ' '.join([text] + [
            section.title + ' ' + (section.text or '')
            for section in self.page.contentsection_set.all()
        ])


class ContentSection(models.Model):
    # This is a model which will be registered inline so that you can edit it
    # directly from the page's admin screen.
    #
    # This ForeignKey to `pages.Page` is entirely necessary in order to make
    # inlines work. Note that it is to the *Page* itself and not the content
    # model!
    page = models.ForeignKey(
        'pages.Page',
        on_delete=models.CASCADE,
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
