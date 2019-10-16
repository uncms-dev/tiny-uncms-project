'''Views used by the tiny project's news app.'''

from cms.views import PageDetailMixin
from django.views.generic import DetailView, ListView

from .models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(
            page__page=self.request.pages.current,
        )


class ArticleDetailView(PageDetailMixin, DetailView):

    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(
            page__page=self.request.pages.current,
        )
