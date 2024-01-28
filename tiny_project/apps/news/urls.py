from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
]
