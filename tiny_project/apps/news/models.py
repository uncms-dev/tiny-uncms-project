"""
Models used by the tiny project's news app.

This will demonstrate UnCMS's PageBase helper class, per-page URL routing,
and others.
"""

# UnCMS plays nice with standard Django fields too :) There is no need for
# special field types on your content models.
from django.db import models
from django.utils.timezone import now

# We'll do a fuller explanation of these fields later. Search ahead if you're
# impatient. But, we want images...
from uncms.media.models import ImageRefField

# ...and a nice HTML editor, and two things we'll explain later...
from uncms.models import HtmlField, PageBase, PageBaseManager

# ...and we want to create a page content model...
from uncms.pages.models import ContentBase


class NewsFeed(ContentBase):
    """
    A stream of news articles.
    """

    # On the "Add a page" screen, the available page types are broken down
    # into classifiers. Really, this is just a heading under which this page
    # type will appear. It is a good idea to use 'apps' for content models
    # whose primary purpose it is to display links to other content, and
    # 'content' for content models for which the content is primarily on-page.
    # That's just convention for us; you can actually name this anything you
    # like.
    #
    # This will be title-cased when it is rendered in the admin.
    classifier = "content"

    # An icon at this location (under your static files directory) will be
    # displayed in the "Add a page" screen. ContentBase has a default icon,
    # but you can make your own icons too. This should be 96x96 at the moment,
    # but making it a little larger wouldn't hurt.
    #
    # Want some help? At Onespacemedia we made a whole lot of icons in the
    # same style which are perfect for the 'Add a page' screen. Go get one for
    # your app here: https://github.com/onespacemedia/cms-icons
    icon = "icons/news.png"

    # The urlconf used to power this content's views. We don't *have* to
    # specify this at all! If we did not then it would simply render a
    # template at <app_label>/<model_name>.html. But this allows us to have
    # have complete control of everything below this page in the URL
    # structure.
    #
    # In fact, even the default view mentioned above comes from a urlconf on
    # ContentBase, with an extremely simple TemplateView derivative.
    urlconf = "tiny_project.apps.news.urls"

    # ContentBase derivatives don't have ModelAdmins at all - their fields get
    # automatically patched into the form for the *Page*. But, we like
    # fieldsets! So we simply define them on the model. There's no need to
    # list the various SEO and publication fields on the Page here; these will
    # be added automatically.
    fieldsets = [
        (
            "Settings",
            {
                "fields": ["per_page"],
            },
        ),
    ]

    # And on to some model fields. The great part of the simple data model of
    # UnCMS is that it makes it really easy to define page settings that are
    # not visible to non-admin users. Here, we want admin control over how
    # will be displayed on a page. We'll be able to  access this later in the
    # `get_paginate_by` function in our view.
    #
    # Another typical example would be deciding where a form on a "Contact"
    # content model would send emails to. No need to hard-code anything! Some
    # other CMSes make this extraordinarily hard; here you're just writing
    # Django.
    #
    # Notice also that UnCMS works perfectly with standard Django model
    # fields.

    per_page = models.IntegerField(
        verbose_name="Articles per page",
        default=12,
    )

    # This might seems strange (this is the same as the inherited behaviour),
    # but our linters mandate that every model has its own __str__ method :)
    def __str__(self):
        return self.page.title


#
# I would urge you to read down to the 'Article' model below, then read this
# comment.
#
# ...and now that you are back, let's talk about PageBaseManager. This is the
# default manager for anything that inherits from PageBase; it ensures that
# anything set to offline (is_online == False) does not get displayed anywhere
# except in preview mode or in the admin. But we want to hide news articles
# that have a publication date set to the future; that gives admins a way of
# building up a queue of articles to publish. Let's write a simple derivative
# of PageBaseManager that does this for us.
#
class ArticleManager(PageBaseManager):
    def select_published(self, queryset):
        return super().select_published(queryset).exclude(date__gt=now())


#
# OK, let's talk about PageBase here. It's a helper (abstract) model to make
# it easier for you to have article-like models on the fields. It has nearly
# all the fields that the Page model itself does, but does not consider itself
# part of any hierarchy. Here's what you get:
#
# * A title and slug
# * Online/offline controls (enforced by the manager)
# * OpenGraph and Twitter card fields.
# * SEO fields like meta descriptions and a title override
#
# If you only need the publication controls, inherit from OnlineBase.
#
# If you need the SEO/OpenGraph fields as well, inherit from SearchMetaBase
# (this inherits from OnlineBase, so you get that for free). This is useful
# for models wherein the "title" of a page comes from multiple fields; for
# example, a page about a person wherein the title of a page needs to be
# formed from their first and last names.
#
class Article(PageBase):
    """A simple news article."""

    objects = ArticleManager()

    # We want to be able to have multiple types of news feed. For example,
    # we might want to have a page of articles called "News" (what your cat
    # did today) vs "Blog" (insights on cat behaviour). Because we have access
    # to the current page and its content object in our request, we can filter
    # only the news articles which have this ForeignKey set to the currently
    # active page - alternatively put, that "belong" to it.
    page = models.ForeignKey(
        "news.NewsFeed",
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        verbose_name="News feed",
    )

    # ImageRefField is a ForeignKey to `media.File`, but it uses a raw ID
    # widget by default, and is constrained to only select files that appear
    # to be images (just a regex on the filename). You also have FileRefField
    # that doesn't do the "looks like an image" filtering, but does use the
    # raw ID widget.
    image = ImageRefField(
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    # HtmlField is like a TextField, but gives you a full-featured TinyMCE
    # WYSIWYG editor in your admin. This is just for your convenience.
    # HtmlField is not used internally in UnCMS, and nothing about an UnCMS
    # project requires that you use it. You can use your own favourite field
    # with your own favourite editor here. (BUT YOU SHOULD USE OURS REALLY)
    content = HtmlField()

    # Some more standard Django fields :)
    date = models.DateTimeField(
        default=now,
    )

    summary = models.TextField(
        blank=True,
    )

    class Meta:
        # Not an UnCMS thing, but if we have two articles assigned to the same
        # page (as above) they'll both have the same URL, and the
        # queryset.get(...) will throw MultipleObjectsReturned. Let's stop
        # that from happening.
        unique_together = [["page", "slug"]]
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # OK, so once we have our urlconf on our content object, whereever we
        # we have access to that content, we reverse those URLs almost exactly
        # as we use django's standard reverse.
        #
        # self.page here is our NewsFeed (content model), and self.page.page
        # is the page to which our content model is attached.
        return self.page.page.reverse(
            "article_detail",
            kwargs={
                "slug": self.slug,
            },
        )
