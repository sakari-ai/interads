from core.exception.exceptions import WrongInputException


class ZeroparkObject:
    def __init__(self, result):
        self.page = result["page"]
        self.total = result["total"]
        self.limit = result["limit"]
        self.elements = result["elements"]

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.page == other.page and self.total == other.total and self.limit == other.limit and self.elements == other.elements:
            return True
        return False
    def __str__(self):
        return '{}-{}-{}-{}'.format(self.page, self.total, self.limit, self.elements)