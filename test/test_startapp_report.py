import unittest
import httpretty
from services.responses.startapp_report_response import StartAppReportObject
from services.startapp_report import StartAppReportService


class TestFunction(unittest.TestCase):
    @httpretty.activate
    def test_get_report(self):
        httpretty.register_uri(httpretty.GET,
                               "http://api.startapp.com/adv/report/1.0?partner=1&token=1&startDate=1&endDate=1",
                               body='{"logs": "", "data": "yes"}')
        response = StartAppReportService().get_report(1,1,1,1)
        res = {"logs": "", "data": "yes"}
        self.assertEqual(response, StartAppReportObject(res))

    @httpretty.activate
    def test_get_report_with_dimension(self):
        httpretty.register_uri(httpretty.GET,
                               "http://api.startapp.com/adv/report/1.0?partner=1&token=1&startDate=1&endDate=1&dimension=country&dimension=date",
                               body='{"logs": "", "data": "yes"}')
        c =['country', 'date']
        response = StartAppReportService().get_report(1, 1, 1, 1, dimensions=c)
        res = {"logs": "", "data": "yes"}
        self.assertEqual(response, StartAppReportObject(res))

if __name__ == '__main__':
    unittest.main()

