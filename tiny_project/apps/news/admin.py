'''Admin settings for the tiny news app.'''

# PageBaseAdmin defines some useful fieldsets, which we will use later. You
# should always use this for models that inherit from PageBase.
#
# As it has title and slug fields, it will automatically prepopulate the
# latter from the former - no need to add prepopulated_fields yourself. Yay!
#
# Because PageBaseAdmin inherits from OnlineBaseAdmin, it'll also obey
# the ONLINE_DEFAULT setting (whether newly objects are on or offline by
# default).

from cms.admin import PageBaseAdmin
from django.contrib import admin

from .models import Article, NewsFeed


@admin.register(Article)
class ArticleAdmin(PageBaseAdmin):
    # Our default will only search the title.
    search_fields = PageBaseAdmin.search_fields + ('content', 'summary',)

    list_display = ['title', 'date', 'is_online']
    list_editable = ['is_online']

    fieldsets = [
        (None, {
            'fields': ['title', 'date', 'slug', 'page', 'image', 'content', 'summary'],
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
        PageBaseAdmin.OPENGRAPH_FIELDS,
        PageBaseAdmin.OPENGRAPH_TWITTER_FIELDS,
    ]

    def get_form(self, request, obj=None, **kwargs):
        '''
        We don't *have* to do this, and one wonders if it is slightly out
        of scope for a tiny demo CMS project. But it is kind to have sensible
        defaults :)
        '''
        form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['page'].initial = NewsFeed.objects.first()
        return form
