from django.urls import reverse_lazy
from uncms import robots


class RobotsTxtView(robots.RobotsTxtView):
    # `uncms.views.RobotsTxtView` gives a slightly over-engineered way to
    # build a robots.txt for your site. You can just forgo all this and use
    # `uncms.views.TextTemplateView(template_name='robots.txt')` in your
    # urlconf instead. But RobotsTxtView will handle the fussiness around
    # whitespace so you don't have to.
    #
    # First, our sitemap. This can be a string, something like a string (such
    # as the result of reverse_lazy), or a list of either of the previous two.
    # This could just as easily be any of:
    #
    #   sitemaps = '/sitemap.xml'
    #   sitemaps = ['/sitemap.xml']
    #   sitemaps = reverse_lazy('django.contrib.sitemaps.views.sitemap')
    #
    # Which means it handles multiple sitemaps, too:
    #
    #   sitemaps = ['/sitemap.xml', '/sitemap-pages.xml']
    #
    # Using the value of SITE_DOMAIN, sitemap URLs will be normalised to a
    # full URL including protocol (assumed to be `https` when DEBUG is False)
    # and domain.
    sitemaps = [reverse_lazy("django.contrib.sitemaps.views.sitemap")]

    # Let's add some rules for user agents.
    user_agents = [
        robots.UserAgentRule(
            # "agent" can be either a single bot (a string), or a list of
            # strings.
            agent=["Megabot 9000", "Turbotron 9001"],
            allow="/",
            # Disallow can either be a single path, or a list of paths. Paths
            # are forced to strings so they can be either strings or lazy
            # objects as returned by reverse_lazy.
            disallow=[reverse_lazy("admin:index")],
        ),
        robots.UserAgentRule(
            agent="Badbot",
            disallow="/",
            # You may specify a comment which will be placed immediately above
            # the rule.
            comment="Go away",
        ),
    ]
