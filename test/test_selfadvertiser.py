import unittest
import httpretty
import json

from services.selfadvertiser import SelfAdvertiserService
from services.responses.selfadvertise_response import SelfAdvertiserObject
from core.exception.exceptions import WrongInputException


class TestFunction(unittest.TestCase):
    @httpretty.activate
    def test_get_all_campaigns(self):
        body_test = {"Data": "abc"}
        httpretty.register_uri(httpretty.GET,
                               "https://app.selfadvertiser.com/api/v1/campaigns/0?token=cf0edf6a3ff26b2a646f5b1a07eac2ae",
                               body=json.dumps(body_test))
        res = SelfAdvertiserService("cf0edf6a3ff26b2a646f5b1a07eac2ae").get_all_campaigns()
        self.assertEqual(res, SelfAdvertiserObject(body_test))

    @httpretty.activate
    def test_get_by_campaigns_id(self):
        body_test = {"Data": "abc"}
        httpretty.register_uri(httpretty.GET,
                               "https://app.selfadvertiser.com/api/v1/campaigns/~tUQKE1Egx5g,~z9WeghNkdlM?token=cf0edf6a3ff26b2a646f5b1a07eac2ae",
                               body=json.dumps(body_test))
        res = SelfAdvertiserService("cf0edf6a3ff26b2a646f5b1a07eac2ae").get_by_campaigns_id(['~tUQKE1Egx5g','~z9WeghNkdlM'])
        self.assertEqual(res, SelfAdvertiserObject(body_test))

    @httpretty.activate
    def test_update_status_campaigns(self):
        body_test = {"Data": "abc"}
        httpretty.register_uri(httpretty.PUT,
                               "https://app.selfadvertiser.com/api/v1/campaigns/~tUQKE1Egx5g/action/resume?token=cf0edf6a3ff26b2a646f5b1a07eac2ae",
                               body=json.dumps(body_test))
        res = SelfAdvertiserService("cf0edf6a3ff26b2a646f5b1a07eac2ae").update_status_campaigns("~tUQKE1Egx5g", "resume")
        self.assertEqual(res, SelfAdvertiserObject(body_test))

    @httpretty.activate
    def test_block_source(self):
        body_test = {"Data": "abc"}
        httpretty.register_uri(httpretty.POST,
                               "https://app.selfadvertiser.com/api/v1/campaigns/~tUQKE1Egx5g,~z9WeghNkdlM/sources/black/123456,654321?token=cf0edf6a3ff26b2a646f5b1a07eac2ae",
                               body=json.dumps(body_test))
        res = SelfAdvertiserService("cf0edf6a3ff26b2a646f5b1a07eac2ae").block_source(["~tUQKE1Egx5g",'~z9WeghNkdlM'],["123456","654321"])
        self.assertEqual(res, SelfAdvertiserObject(body_test))


if __name__ == '__main__':
    unittest.main()