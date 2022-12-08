from django.apps import AppConfig
from django.conf import settings

class DjangoPluginsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_plugins'
    def ready(self, *args, **kwargs):
        installed_plugins = getattr(settings, "INSTALLED_PLUGINS", {})
        assert len(installed_plugins) > 0, "You havent installed any plugin yet, for using this module please install a plugin first."
