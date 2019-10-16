"""URLs used by the CMS news app."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^(?P<slug>[^/]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
]
