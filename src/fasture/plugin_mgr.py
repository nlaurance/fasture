import pluggy
from fasture import specs


def get_plugin_manager():
    pm = pluggy.PluginManager("fasture")
    pm.add_hookspecs(specs)
    pm.load_setuptools_entrypoints("fasture")
    # pm.register(default_task, name="HomeMade")
    return pm
