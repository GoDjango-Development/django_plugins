from django.utils.module_loading import import_string
from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from functools import lru_cache
import json

@lru_cache
def get_plugin(name):
    plugin = settings.INSTALLED_PLUGINS.get(name, None)
    if plugin is None:
        raise ImproperlyConfigured("%s seems to be None or is not configured... Read your plugin documentation to see how to use it"%name)
    return plugin

def get_pulgin_conf(name, *args, default=None,):
    args = list(args)
    plugin_confs = _get_pulgin_conf(conf=get_plugin(name), args=args)
    if hasattr(plugin_confs, "__iter__"): # if it is iterable
        for index in range(len(plugin_confs)):
            plugin_confs[index] = autoresolve(plugin_confs[index])
    return plugin_confs

def _get_pulgin_conf(conf, args=list(), default=None):
    """This iterates over a dict until the end"""
    try:
        index = args.pop(0)
        if type(index) is list:
            "split a tree"
            res = []
            for i in index:
                res.append(_get_pulgin_conf(conf=conf.get(i), args=args.copy())) # copy to each leaf of the tree has its own copy
            return res # once a list like array is given the main leaf stops iterating over itself so when the loop finish it means both args stack were exhausted so the resulting part must be an array of results
        return _get_pulgin_conf(conf=conf.get(index), args=args)
    except IndexError:
        if len(args) == 0:
            return conf
        return default

def autoresolve(variable, *args, **kwargs):
    if type(variable) is str and "." in variable: # dotted path
        try:
            variable = variable.split("%", 2)
            if len(variable) > 1:
                args = json.loads(variable.pop())
                kwargs = args.get('kwargs', {})
                args = args.get("args", ())
            variable = import_string(variable.pop(0))
            if callable(variable) and not hasattr(variable, "__init__"): # a callable but not a callable class
                variable = variable(*args, **kwargs) # call the resulting variable
            elif issubclass(variable, models.Model):
                variable = variable.objects.filter(**kwargs).values_list(flat=True, *args).first()
            elif callable(variable) and hasattr(variable, "__init__"): # callable class
                variable = variable(*args, **kwargs) # call the resulting variable
        except Exception as error: # if we were wrong and its not a dotted part then follow
            variable = None
            #print("error: ", error)
            pass
    elif callable(variable):
        variable = variable(*args, **kwargs) # call the resulting variable
    return variable