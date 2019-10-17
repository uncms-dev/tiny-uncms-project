# We'll explain PageDetailMixin later, but the short version is that if you
# are displaying a DetailView for a model that inherits from PageBase, you
# definitely want to inherit from PageDetailMixin too.
from cms.views import PageDetailMixin
from django.views.generic import DetailView, ListView

from .models import Article


class ArticleListView(ListView):
    '''Displays a list of articles.'''
    # ^ hey, don't write docstrings like this. Unless you have a class named
    # ArticleListView that does not list articles, in which case you have
    # other, deeper-seated problems. :)
    model = Article

    def get_paginate_by(self, queryset):
        # As mentioned in models.py, we have a simple setting on the content
        # model to control how many news articles are being shown by page
        # (just a plain old IntegerField). In there, we mentioned that we
        # would have access to the current page in the view. But how?
        #
        # Simples: PageMiddleware patches the current page tree on to the
        # request (actually an instance of RequestPageManager).
        # `pages.current` is the currently active page, i.e. the page to which
        # our current content object is attached. So all we need to do to make
        # it paginate by our admin-defined amount is...
        return self.request.pages.current.content.per_page

    def get_queryset(self):
        # As also mentioned in models.py, we only want to list those news
        # articles that "belong" to the current page. Once again, our
        # PageMiddleware and its friend RequestPageManager make this really
        # easy.
        return super().get_queryset().filter(
            page__page=self.request.pages.current
        )

# Let's talk about PageDetailMixin.
#
# We have all those nice fields for SEO, OpenGraph, etc which will be rendered
# by the appropriate template tags. To ensure that the keys we need are in the
# context, simply inherit your DetailView derivative from PageDetailMixin as
# well!
#
# Likewise, there's a SearchMetaDetailMixin for models that inherit from
# SearchMetaBase.
class ArticleDetailView(PageDetailMixin, DetailView):
    '''Displays a single article.'''

    # We're kinda repeating outself with this; we could probably inherit both
    # of these views from ArticleMixin. But we're trying to keep these
    # examples as simple as possible. Also, copy-pasting is faster!

    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(
            page__page=self.request.pages.current,
        )
