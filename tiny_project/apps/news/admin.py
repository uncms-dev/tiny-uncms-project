"""Admin settings for the CMS news app."""
from cms.admin import PageBaseAdmin
from django.contrib import admin

from .models import Article, NewsFeed


@admin.register(Article)
class ArticleAdmin(PageBaseAdmin):
    search_fields = PageBaseAdmin.search_fields + ('content', 'summary',)

    list_display = ['title', 'date', 'is_online']
    list_editable = ['is_online']

    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'page', 'content', 'summary'],
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
        PageBaseAdmin.OPENGRAPH_FIELDS,
        PageBaseAdmin.OPENGRAPH_TWITTER_FIELDS,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['page'].initial = NewsFeed.objects.first()
        return form
