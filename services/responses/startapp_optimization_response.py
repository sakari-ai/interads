from core.exception.exceptions import InputException

class StartAppOptimizationObject:
    def __init__(self, res):
        for num in res:
            if num not in ["data", "summary"]:
                raise InputException("Response has unexpected field: {}".format(num))
        self.data = res['data']
        self.summary = res['summary']

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.data == other.data and self.summary == other.summary:
            return True
        return False
