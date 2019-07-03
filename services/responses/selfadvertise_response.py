from core.exception.exceptions import WrongInputException

class SelfAdvertiserObject:
    def __init__(self, res):
        self.Data = res["Data"]

    def __str__(self):
        return '{}'.format(self.Data)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.Data == other.Data:
            return True
        return False
