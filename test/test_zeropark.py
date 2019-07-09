import unittest
import httpretty
import json

from services.zeropark import ZeroparkService
from services.responses.zeropark_response import ZeroparkObject
from core.exception.exceptions import InputException


class TestFunction(unittest.TestCase):

    @httpretty.activate
    def test_get_by_campaigns_id_with_default_interval(self):
        body_test = {"page": "abc", "total": "90", "limit": "100", "elements": "abxcd" }
        httpretty.register_uri(httpretty.GET,
                               "https://panel.zeropark.com/api/stats/campaign/a1b9c834-8d2e-11e9-8a1b-12077332b422/details?interval=TODAY",
                               body=json.dumps(body_test))
        res = ZeroparkService('AAABaqEcUvDsCyK7PToeCSw9X2NiLwHY2jnPTMaiz3VKmiiW2jyIvrA/wYlaVryhRdUUVuAkZg+a1bcTI3bYFQ==').get_by_campaigns_id_with_default_interval(
            'a1b9c834-8d2e-11e9-8a1b-12077332b422', 'TODAY'
        )
        self.assertEqual(res, ZeroparkObject(body_test))

    @httpretty.activate
    def test_get_by_campaigns_id_with_custom_interval(self):
        body_test = {"page": "abc", "total": "90", "limit": "100", "elements": "abxcd"}
        httpretty.register_uri(httpretty.GET,
                               "https://panel.zeropark.com/api/stats/campaign/a1b9c834-8d2e-11e9-8a1b-12077332b422/details?interval=CUSTOM&startDate=4/1/2018&endDate=5/1/2018",
                               body=json.dumps(body_test))
        res = ZeroparkService(
            'AAABaqEcUvDsCyK7PToeCSw9X2NiLwHY2jnPTMaiz3VKmiiW2jyIvrA/wYlaVryhRdUUVuAkZg+a1bcTI3bYFQ==').get_by_campaigns_id_with_custom_interval(
            'a1b9c834-8d2e-11e9-8a1b-12077332b422', '4/1/2018', '5/1/2018'
        )
        self.assertEqual(res, ZeroparkObject(body_test))

if __name__ == '__main__':
    unittest.main()