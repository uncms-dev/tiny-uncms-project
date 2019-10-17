from cms.apps.pages.admin import page_admin
# You can use any of Django's standard inline classes here. We're using
# osm_jet's JetCompactInline because we have it in this project and it workis
# a lot nicer, giving drag and drop ordering :)
from osm_jet.admin import JetCompactInline

from .models import Content, ContentSection


# Note that the inline model must inherit from Django inlines, not
# ModelAdmin.
class ContentSectionInline(JetCompactInline):
    model = ContentSection

# And this, is all you need to do to get an inline registered for a given
# content type.
page_admin.register_content_inline(Content, ContentSectionInline)
