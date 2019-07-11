from  django import conf
from polls.apps import PollsConfig

def kingadmin_auto_discover():
    for app_name in conf.settings.INSTALLED_APPS:
        # mod = importlib.import_module(app_name, 'kingadmin')
        try:
            app_name = app_name
            mod = __import__('%s.kingadmin' % app_name)
            #print(mod.kingadmin)
        except ImportError as e:
            print(e)

