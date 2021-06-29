class Phone():
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'


class SmartPhone(Phone):
    def run_app(self, app):
        return f'Running {app}'


class IPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()
