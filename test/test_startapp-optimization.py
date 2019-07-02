import unittest
import httpretty
from services.responses.startapp_optimization_response import StartAppOptimizationObject
from services.startapp_optimization import StartAppOptimizationService


class TestFunction(unittest.TestCase):
    @httpretty.activate
    def test_update_targeting(self):
        httpretty.register_uri(httpretty.PUT,
                               "https://api.startapp.com/adv/campaignOptimization/1.0/blacklist?partner=1&token=1",
                               body='{"success":true}')
        response = StartAppOptimizationService(1, 1).update_campaign_targeting(1, 1, 1, 1)
        self.assertEqual(response, "SUCCEEDED!")

    @httpretty.activate
    def test_update_optimization(self):
        httpretty.register_uri(httpretty.PUT,
                               "https://api.startapp.com/adv/campaignOptimization/1.0/optimize?partner=1&token=1",
                               body='{"success":true}')
        response = StartAppOptimizationService(1, 1).update_campaign_optimization(1, 1)
        self.assertEqual(response, "SUCCEEDED!")

    @httpretty.activate
    def test_get_optimization(self):
        httpretty.register_uri(httpretty.POST,
                               "https://api.startapp.com/adv/campaignOptimization/1.0/optimize?partner=1&token=1",
                               body='{"data":"yes", "summary": "yes"}')
        response = StartAppOptimizationService(1, 1).get_campaign_optimization(1, 1, 1, 2, 3, 4, 5)
        res = {"data": "yes", "summary": "yes"}
        self.assertEqual(response, StartAppOptimizationObject(res))


if __name__ == '__main__':
    unittest.main()

