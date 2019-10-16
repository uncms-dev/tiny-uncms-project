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

    # The urlconf used to power this content's views.
    urlconf = 'tiny_project.apps.news.urls'

    fieldsets = [
        (None, {
            'fields': ['per_page'],
        }),
    ]

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
