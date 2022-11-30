from django.apps import AppConfig


class DjangoPluginsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_plugins'
    def ready(self, *args, **kwargs):
        #TODO: Implement here settings.py INSTALLED_PLUGINS functionalities
        pass
