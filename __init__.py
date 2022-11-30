from django.utils.module_loading import import_string
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def get_plugin(name):
    plugin = settings.INSTALLED_PLUGINS.get(name, None)
    if plugin is None:
        raise ImproperlyConfigured("%s seems to be None or is not configured... Read your plugin documentation to see how to use it"%name)
    return plugin