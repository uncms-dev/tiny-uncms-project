from uncms.sitemaps import registered_sitemaps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.contenttypes import views as contenttypes_views
from django.contrib.sitemaps import views as sitemaps_views
from django.urls import include, path, re_path

admin.autodiscover()


urlpatterns = [
    # Standard admin URLs.
    path('admin/', admin.site.urls),

    # Permalink redirection service. Parts of UnCMS, specifically HTML
    # filtering, depend on this.
    re_path(r'^r/(?P<content_type_id>\d+)-(?P<object_id>[^/]+)/$', contenttypes_views.shortcut, name='permalink_redirect'),

    # Google sitemap service. UnCMS models play nice with these too!
    re_path(r'^sitemap.xml$', sitemaps_views.index, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # And not just with pages; anything that has a get_absolute_url method can
    # register itself, but it works especially well with anything that inherits
    # from our PageBase model.
    re_path(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('library/', include('uncms.media.urls', namespace='media_library')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
