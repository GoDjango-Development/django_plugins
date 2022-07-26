PLUGIN_NAME = "YOUR PLUGIN NAME"
INSTALLED_PLUGINS = {
    "PLUGIN_NAME": {
            "admin_parents" : {
                "YourClassName": "dotted.path.to.Parent",
                "YourNClassesNames": "ndotted.path.to.Parents",
            },
            "identifier": "dotted.path.to.IdentifierClass",
            "id_resolver": "dotted.path.to.IdResolver",
            "sites": ("dotted.path.to.SiteToRegister1", "dotted.path.to.SiteToRegisterN")
        }
}