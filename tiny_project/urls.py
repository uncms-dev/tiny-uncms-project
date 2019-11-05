from cms.sitemaps import registered_sitemaps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.contenttypes import views as contenttypes_views
from django.contrib.sitemaps import views as sitemaps_views

admin.autodiscover()


urlpatterns = [

    # Standard admin URLs.
    url(r'^admin/', admin.site.urls),

    # Permalink redirection service. Parts of the CMS, specifically HTML
    # filtering, depend on this.
    url(r'^r/(?P<content_type_id>\d+)-(?P<object_id>[^/]+)/$', contenttypes_views.shortcut, name='permalink_redirect'),

    # Google sitemap service. Our CMS models play nice with these too!
    url(r'^sitemap.xml$', sitemaps_views.index, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # And not just with pages; anything that has a get_absolute_url method can
    # register itself, but it works especially well with anything that inherits
    # from our PageBase model.
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
