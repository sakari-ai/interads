from core.exception.exceptions import WrongInputException


class ExchangeRateObject:
    def __init__(self, result):
        for num in result:
            if num not in ["base", "rates", "date", "start_at", "end_at"]:
                raise WrongInputException('WRONG INPUT')
        self.base = result['base']
        self.rates = result['rates']
        self.date = None
        self.start_at = None
        self.end_at = None
        if "date" in result:
            self.date = result['date']
        if "end_at" in result:
            self.end_at = result['end_at']
        if "start_at" in result:
            self.start_at = result['start_at']

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.base, self.rates, self.date, self.start_at, self.end_at)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.base == other.base and self.rates == other.rates and self.date == other.date and \
                self.start_at == other.start_at and self.end_at == other.end_at:
            return True
        return False


