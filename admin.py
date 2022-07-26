from django.conf import settings
from django.utils import module_loading
from django.contrib import admin

# Register your models here.

# Plugin configuration
sites = ()
admin_parents = {}

if hasattr(settings, "INSTALLED_PLUGINS") and type(settings.INSTALLED_PLUGINS) is dict:
    TRANSLATOR_PLUGIN = settings.INSTALLED_PLUGINS.get("TRANSLATOR", {})
    sites = TRANSLATOR_PLUGIN.get("sites", sites)
    admin_parents = TRANSLATOR_PLUGIN.get("admin_parents", admin_parents)
    for key in admin_parents.keys():
        admin_parents[key] = module_loading.import_string(admin_parents[key])

class PluginAdmin(admin_parents.get("None")):
    pass

for site in sites:
    site_class = module_loading.import_string(site)
    site_class.register(CacheTranslations, CacheTranslationAdmin)
