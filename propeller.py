from services.resource import APIResource, ResponseHandler, Configuration
from amp.services.base import ServiceBuilder


class PropellerClient(APIResource):
    def __init__(self):
        config = Configuration("https://ssp-api.propellerads.com/v5", auth_handler=False, handler=None, service_name='Propellerads Service(AMP)')
        super().__init__(config)


    def get_adv_statistics(self):
        querystring = '/adv/statistics'
        return self.get(querystring)
