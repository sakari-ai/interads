import unittest
import httpretty
import json

from services.propeller import PropellerService
from services.responses.propeller_response import PropellerStatObject,PropellerCampaignObject
from core.exception.exceptions import InputException


class TestFunction(unittest.TestCase):
    @httpretty.activate
    def test_request_adv_statistics(self):
        body_test = {"result": "abc",  "meta": "xyz"}
        httpretty.register_uri(httpretty.GET,
                               "https://ssp-api.propellerads.com/v5/adv/statistics",
                               body=json.dumps(body_test))
        res = PropellerService().get_adv_statistics()
        self.assertEqual(res, PropellerStatObject(body_test))

    @httpretty.activate
    def test_get_by_campaignID(self):
        body_test = {"data": "dataTest"}
        httpretty.register_uri(httpretty.GET,
                               "https://ssp-api.propellerads.com/v5/adv/campaigns/123456",
                               body=json.dumps(body_test))
        res = PropellerService().get_by_campaignsID('123456')
        self.assertEqual(res, PropellerCampaignObject(body_test))


if __name__ == '__main__':
    unittest.main()

