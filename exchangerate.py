from services.resource import APIResource, ResponseHandler, Configuration
import json
from amp.services.base import ServiceBuilder

class ExchangeRateClient(APIResource):

    def __init__(self):
        config = Configuration(url, auth_handler=False, handler=None, service_name='Exchange Rate Service(AMP)')
        super().__init__(config)


    def get_latest(self):
        querystring = '/latest'
        return self.get(querystring)


    def get_by_time(self , day , month , year):
        querystring = "/{}-{}-{}".format(year , month , day)
        return self.get(querystring)


    def get_by_base(self , moneyunit):
        querystring = "/latest?base={}".format(moneyunit)
        return self.get(querystring)


    def get_by_symbols(self , moneyunit):
        querystring =  "/latest?symbols={}".format(moneyunit)
        return self.get(querystring)


    def get_by_history(self , day1 , month1 , year1 , day2 , month2 , year2):
        querystring =  "/history?start_at={}-{}-{}&end_at={}-{}-{}".format(year1 , month1 , day1 ,year2 , month2 , day2)
        return self.get(querystring)


# class ExchangeRateBuilder(ServiceBuilder):
#     def get_service(self)
#         if not self.service:
#             return _build_service("https://exchangeratesapi.io/")
#         else return self.service[0]
#
#     def _build_service(self, url)
#         config = Configuration(url, auth_handler=False, handler=None, service_name='Exchange Rate Service(AMP)')
#         service = ExchangeRateClient(config)
#         return service
