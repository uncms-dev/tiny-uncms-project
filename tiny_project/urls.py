from cms.sitemaps import registered_sitemaps
from cms.views import TextTemplateView
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.contenttypes import views as contenttypes_views
from django.contrib.sitemaps import views as sitemaps_views
from django.shortcuts import render
from django.views import generic

admin.autodiscover()


urlpatterns = [

    # Admin URLs.
    url(r'^admin/', include(admin.site.urls)),

    # Jet URLs
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    # Permalink redirection service. Parts of the CMS, specifically HTML
    # filtering, depend on this.
    url(r'^r/(?P<content_type_id>\d+)-(?P<object_id>[^/]+)/$', contenttypes_views.shortcut, name='permalink_redirect'),

    # Google sitemap service.
    url(r'^sitemap.xml$', sitemaps_views.index, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
