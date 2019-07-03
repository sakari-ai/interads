class InteradObject:
    def __init__(self, imp, click, spent):
        self._imp = imp
        self._click = click
        self._spent = spent

    def get_impressions(self):
        return self._imp

    def get_click(self):
        return self._click

    def get_spent(self):
        return self._spent

