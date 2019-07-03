from core.delegation.responsehandler import ResponseHandler
from core.resource import APIResource, Configuration
from services.responses.propeller_response import PropellerStatObject, PropellerCampaignObject


class PropellerService(APIResource):
    def __init__(self):
        config = Configuration("https://ssp-api.propellerads.com/v5", auth_handler=False, handler=PropellerHandler(),
                               service_name='Propellerads Service(AMP)')
        super().__init__(config)

    def get_adv_statistics(self):
        querystring = '/adv/statistics'
        return self.get(querystring)

    def get_by_campaignsID(self, campaignID):
        querystring = '/adv/campaigns/{}'.format(campaignID)
        return self.get(querystring)

class PropellerHandler(ResponseHandler):
    @staticmethod
    def handle(result):
        if result.status_code == 200:
            res = result.json()
            if 'result' in res:
                return PropellerStatObject(res)
            return PropellerCampaignObject(res)
        return result.status_code


