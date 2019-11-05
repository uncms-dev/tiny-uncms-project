from cms.apps.pages.admin import page_admin
from django.contrib.admin import StackedInline

from .models import Content, ContentSection


# Note that the inline model must inherit from Django inlines, not
# ModelAdmin.
class ContentSectionInline(StackedInline):
    model = ContentSection
    extra = 0

# And this, is all you need to do to get an inline registered for a given
# content type.
page_admin.register_content_inline(Content, ContentSectionInline)
