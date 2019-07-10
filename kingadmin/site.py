class BaseAdmin():
    pass


class adminsite():
    def __init__(self):
        self.youwrite = {}

    def register(self,model_class , admin_class=None):
        model = model_class._meta.model_name
        app = model_class._meta.app_label
        if not admin_class:
            admin_class = BaseAdmin()
        else:
            admin_class= admin_class()
        if app not in self.youwrite:
            self.youwrite[app] = {}
        self.youwrite[app][model] = admin_class


site = adminsite()