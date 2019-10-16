'''
Models used by the tiny project's news app.

This will demonstrate the CMS's PageBase helper class.
'''

from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase
from cms.models import HtmlField, PageBase
from django.db import models
from django.utils.timezone import now


class NewsFeed(ContentBase):
    '''
    A stream of news articles.
    '''

    classifier = 'apps'

    icon = 'icons/news.png'

    # The urlconf used to power this content's views. We don't *have* to
    # specify this at all! If we did not then it would simply render a
    # template at <app_label>/<model_name>.html. But this allows us to have
    # have complete control of every
    urlconf = 'tiny_project.apps.news.urls'

    # ContentBase derivatives don't have ModelAdmins at all - their fields get
    # automatically patched into the form for the *Page*. But, we like
    # fieldsets! So we simply define them on the model. There's no need to
    # list the various SEO and publication fields on the Page here; these will
    # be added automatically.
    fieldsets = [
        ('Settings', {
            'fields': ['per_page'],
        }),
    ]

    # And on to some model fields. The great part of the simple data model of
    # onespacemedia-cms is that it makes it really easy to define page
    # settings that are not visible to non-admin users. Here, we want admin
    # control over how many will be displayed on a page. We'll be able to
    # access this later in the view.

    per_page = models.IntegerField(
        verbose_name='Articles per page',
        default=12,
    )

    def __str__(self):
        return self.page.title


class Article(PageBase):
    '''A news article.'''
    page = models.ForeignKey(
        'news.NewsFeed',
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        verbose_name='News feed'
    )

    image = ImageRefField(
        null=True,
        blank=True,
    )

    date = models.DateTimeField(
        default=now,
    )

    summary = models.TextField(
        blank=True,
    )

    content = HtmlField()

    class Meta:
        unique_together = [['page', 'slug']]
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self, page=None):
        '''Returns the URL of the article.'''
        return self.page.page.reverse('article_detail', kwargs={
            'slug': self.slug,
        })
