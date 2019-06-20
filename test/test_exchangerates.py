import unittest
import httpretty
import json

from services.exchangerate import ExchangeService
from services.exchange_response import ExchangeRateObject
from core.exception.exceptions import WrongInputException


class TestFunction(unittest.TestCase):

    @httpretty.activate()
    def test_request_latest(self):
        body_from_latest = {"base": "EUR", "rates": {"BGN": 1.9557}, "date": "2019-06-18"}
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest",
                               body=json.dumps(body_from_latest))
        response_from_main = ExchangeService().get_latest()
        self.assertEqual(response_from_main,ExchangeRateObject(body_from_latest))

    @httpretty.activate
    def test_request_time(self):
        httpretty.activate()
        body_from_time = {"base": "EUR", "rates": {"BGN": 1.9558}, "date": "2007-12-20"}
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/2007-12-20",
                               body=json.dumps(body_from_time))
        response_from_main = ExchangeService().get_by_time('20', '12', '2007')
        self.assertEqual(response_from_main, ExchangeRateObject(body_from_time))

    @httpretty.activate
    def test_request_base(self):
        body_from_base = {"base": "USD", "rates": {"BGN":1.6989}}
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest?base=USD",
                               body=json.dumps(body_from_base))
        response_from_main = ExchangeService().get_by_base('USD')
        self.assertEqual(response_from_main, ExchangeRateObject(body_from_base))

    @httpretty.activate
    def test_request_symbols(self):
        body_from_symbols = {"base": "EUR", "rates": {"USD": 1.1187, "GBP": 0.89403}, "date": "2019-06-18"}
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest?symbols=USD,GBP",
                               body=json.dumps(body_from_symbols))
        response_from_main = ExchangeService().get_by_symbols("USD,GBP")
        self.assertEqual(response_from_main, ExchangeRateObject(body_from_symbols))

    @httpretty.activate
    def test_request_history(self):
        body_from_symbols = {"base": "EUR", "rates": {"USD": 1.1187, "GBP": 0.89403},
                             "start_at": "2018-01-01", "end_at": "2018-09-01"}
        httpretty.register_uri(httpretty.GET,
                               "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01",
                               body=json.dumps(body_from_symbols))
        response_from_main = ExchangeService().get_by_history(1, 1, 2018, 1, 9, 2018)
        self.assertEqual(response_from_main, ExchangeRateObject(body_from_symbols))

    @httpretty.activate
    def test_wrong_input(self):
        with self.assertRaises(WrongInputException):
            body_test = {"wrong": "abc", "input": "xyz"}
            httpretty.register_uri(httpretty.GET,
                                   "https://api.exchangeratesapi.io/latest",
                                   body=json.dumps(body_test))
            ExchangeService().get_latest()


if __name__ == '__main__':
    unittest.main()

