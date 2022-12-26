from uncms.sitemaps import registered_sitemaps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemaps_views
from django.urls import include, path

from tiny_project.views import RobotsTxtView

admin.autodiscover()


urlpatterns = [
    # Standard admin URLs.
    path('admin/', admin.site.urls),

    # Google sitemap service. UnCMS models play nice with these too!
    path('sitemap.xml', sitemaps_views.index, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # And not just with pages; anything that has a get_absolute_url method can
    # register itself, but it works especially well with anything that inherits
    # from our PageBase model.
    path('sitemap-<str:section>.xml', sitemaps_views.sitemap, {'sitemaps': registered_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('library/', include('uncms.media.urls', namespace='media_library')),
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
