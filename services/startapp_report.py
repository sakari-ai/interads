from core.delegation.responsehandler import ResponseHandler
from core.resource import APIResource, Configuration
from services.responses.startapp_report_response import StartAppReportObject
import json

class StartAppReportService(APIResource):
    def __init__(self):
        #self._pid = pid
        #self._token = token
        #self.extend = {"partner": pid, "token": token, "startDate": start, "endDate": end}
        config = Configuration("http://api.startapp.com/adv/report/1.0",
                               auth_handler=False, handler=StartAppReportHandler(),
                               service_name='Startapp Reporting Service')

        super().__init__(config)

    def get_report(self, pid, token, startDate, endDate, dimensions=None, filtering=None, paging=None, header=None):
        """
            dimensions: list of optional dimensions
            filtering: dict {"dimension" : "value"}
            paging: boolean for pagingEnabled
            header: boolean for header
        """
        options = "?partner={}&token={}&startDate={}&endDate={}".format(pid,token,startDate,endDate)
        if dimensions:
            for d in dimensions:
                options = "".join([options, "&dimension={}".format(d)])
        if filtering:
            self.extend.update(filtering)
        if paging:
            self.extend.update({"pagingEnabled": True})
        if header:
            header = {'Accept-Encoding': 'gzip'}
        return self.get("{}".format(options), headers=header)


class StartAppReportHandler(ResponseHandler):
    @staticmethod
    def handle(response):
        res = response.json()
        if res['logs']:
            return res['logs']
        return StartAppReportObject(res)