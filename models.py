from django.db import models

# Create your models here.

identifier_class = None

if hasattr(settings, "INSTALLED_PLUGINS") and type(settings.INSTALLED_PLUGINS) is dict:
    TRANSLATOR_PLUGIN = settings.INSTALLED_PLUGINS.get("TRANSLATOR", {})
    identifier_class = TRANSLATOR_PLUGIN.get("identifier", None)