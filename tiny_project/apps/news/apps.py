from django.apps import AppConfig
from watson import search as watson


class NewsConfig(AppConfig):
    name = 'tiny_project.apps.news'

    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        from cms.models import PageBaseSearchAdapter

        Article = self.get_model('Article')
        watson.register(Article, adapter_cls=PageBaseSearchAdapter)
