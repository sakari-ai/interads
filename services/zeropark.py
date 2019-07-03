from core.delegation.responsehandler import ResponseHandler
from core.resource import APIResource, Configuration
from services.responses.zeropark_response import ZeroparkObject
import requests

class ZeroparkService(APIResource):
    def __init__(self, token):
        self.token = {"api-token": token}
        config = Configuration("https://panel.zeropark.com", auth_handler=False, handler=ZeroparkHandler(),
                               service_name='Zeropark Service(AMP)')
        super().__init__(config)

    def get_by_campaigns_id_with_default_interval(self, campaignId, interval):
        querystring = '/api/stats/campaign/{}/details'.format(campaignId)
        return self.get(querystring , headers=self.token, params={'interval': interval})

    def get_by_campaigns_id_with_custom_interval(self, campaignId, startDate, endDate):
        """

        :param campaignId:
        :param startDate: string with format dd/mm/yyyy
        :param endDate: string with format dd/mm/yyyy
        :return:
        """
        querystring = '/api/stats/campaign/{}/details'.format(campaignId)
        return self.get(querystring, headers=self.token, params={'interval': 'CUSTOM',
                                                                  'startDate': startDate, 'endDate': endDate})

    def get_all_campaigns_with_custom_interval(self, startDate, endDate):
        """

        :param startDate: string with format dd/mm/yyyy
        :param endDate: string with format dd/mm/yyyy
        :return:
        """
        querystring = '/api/stats/campaign/all'
        return self.get(querystring, headers=self.token, params={'interval': 'CUSTOM',
                                                                  'startDate': startDate, 'endDate': endDate})


class ZeroparkHandler(ResponseHandler):
    @staticmethod
    def handle(response):
        res = response.json()
        if 'error' in res:
            return res['error']
        return ZeroparkObject(res)

