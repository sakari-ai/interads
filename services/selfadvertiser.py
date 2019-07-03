from core.delegation.responsehandler import ResponseHandler
from core.resource import APIResource, Configuration
from services.responses.selfadvertise_response import SelfAdvertiserObject
import requests

class SelfAdvertiserService(APIResource):
    def __init__(self , token):
        self.token = {"token": token}
        config = Configuration("https://app.selfadvertiser.com/api/v1", auth_handler=False, handler=SelfAdtiviserHandler(),
                               service_name=' Service(AMP)')
        super().__init__(config)

    def get_all_campaigns(self):
        querystring = '/campaigns/0'
        return self.get(querystring , params = self.token)

    def get_by_campaigns_id(self , list_id):
        """

        :param list_id: list of strings
        :return:
        """
        buid_string_id = ",".join(list_id)
        querystring ='/campaigns/{}'.format(buid_string_id)
        return self.get(querystring , params = self.token)

    def update_status_campaigns(self , id , action):
        querystring = '/campaigns/{}/action/{}'.format(id, action)
        return self.update(querystring , params = self.token)

    def block_source(self , list_id , list_source):
        """

        :param list_id: list of strings
        :param list_source: list of strings
        :return:
        """
        build_string_id = ",".join(list_id)
        build_string_source = ",".join(list_source)
        querystring = '/campaigns/{}/sources/black/{}'.format(build_string_id,build_string_source)
        return self.create(querystring , params = self.token)

class SelfAdtiviserHandler(ResponseHandler):
    @staticmethod
    def handle(response):
        if response.status_code == 200:
            res = response.json()
            return SelfAdvertiserObject(res)
        return response.status_code

