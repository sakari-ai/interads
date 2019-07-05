

class StartAppReportObject:
    def __init__(self, result):
        self.data = result["data"]

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.data == other.data:
            return True
        return False