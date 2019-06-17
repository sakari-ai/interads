from amp.services.Propeller import PropellerClient
import unittest
import requests
import httpretty
import mock

class test_function(unittest.TestCase):

    def test_request_adv_statistics_by_using_httprety(self):
        httpretty.activate()
        body_from_adv_statistics = '{"base":"EUR","rates":{"BGN":1.9558},"date":"2019-06-14"}'
        httpretty.register_uri(httpretty.GET, "https://ssp-api.propellerads.com/v5/adv/statistics", body = body_from_adv_statistics)
        Response_from_main = PropellerClient("https://ssp-api.propellerads.com/v5").get_adv_statistics()
        fake_response = requests.request("GET" , url = "https://ssp-api.propellerads.com/v5/adv/statistics" )
        self.assertEqual(Response_from_main,fake_response.text)
        httpretty.disable()

    
   
    

if __name__ == '__main__': 
    unittest.main() 
