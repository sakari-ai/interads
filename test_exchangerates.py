import unittest
import requests
import httpretty
import mock
from amp.services.exchangerate import exchangeService

class test_function(unittest.TestCase):
    def test_request_latest(self):
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_latest()
        self.fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest" )
        self.assertEqual(Response_from_main , self.fake_response.text)


    def test_request_latest_by_using_httprety(self):
        httpretty.activate()
        body_from_latest = '{"base":"EUR","rates":{"BGN":1.9558},"date":"2019-06-14"}'
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest", body = body_from_latest)
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_latest()
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest" )
        self.assertEqual(Response_from_main,fake_response.text)
        httpretty.disable()


    def test_request_time(self):
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_time('20' , '12' , '2007')
        self.fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/2007-12-20")
        self.assertEqual(Response_from_main , self.fake_response.text)


    def test_request_time_by_using_httprety(self):
        httpretty.activate()
        body_from_time = '{"base":"EUR","rates":{"BGN":1.9558},"date":"2007-12-20"}'
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/2007-12-20", body = body_from_time)
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_time('20' , '12' , '2007')
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/2007-12-20" )
        self.assertEqual(Response_from_main,fake_response.text)
        httpretty.disable()


    def test_reqest_base(self):
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_base("USD")
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest?base=USD" )
        self.assertEqual(Response_from_main , fake_response.text)


    def test_reqest_base_by_using_httprety(self):
        httpretty.activate()
        body_from_base = '{"base":"EUR", "rates":{"BGN":1.6989}}'
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest?base=USD", body = body_from_base)
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_base('USD')
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest?base=USD" )
        self.assertEqual(Response_from_main,fake_response.text)
        httpretty.disable()


    def test_reqest_symbols(self):
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_symbols("USD","GBP")
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP" )
        self.assertEqual(Response_from_main , fake_response.text)


    def test_reqest_symbols_by_using_httprety(self):
        httpretty.activate()
        body_from_symbols = '{"base":"EUR", "rates":{"BGN":1.6989}, "symbols" : {"ILS","JPY"}}'
        httpretty.register_uri(httpretty.GET, "https://api.exchangeratesapi.io/latest?symbols=USD,GBP", body = body_from_symbols)
        Response_from_main = exchangeService("https://api.exchangeratesapi.io").get_by_symbols("USD","GBP")
        fake_response = requests.request("GET" , url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP" )
        self.assertEqual(Response_from_main,fake_response.text)
        httpretty.disable()
        

if __name__ == '__main__':
    unittest.main()
