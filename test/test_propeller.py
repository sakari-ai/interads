import unittest
import httpretty
import json

from services.propeller import PropellerService
from services.responses.propeller_response import PropellerStatObject
from core.exception.exceptions import WrongInputException


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
    def test_wrong_input(self):
        with self.assertRaises(WrongInputException):
            body_test = {"wrong": "abc",  "input": "xyz"}
            httpretty.register_uri(httpretty.GET,
                                   "https://ssp-api.propellerads.com/v5/adv/statistics",
                                   body=json.dumps(body_test))
            PropellerService().get_adv_statistics()



if __name__ == '__main__':
    unittest.main()

