from services.resource import APIResource, ResponseHandler, Configuration
import json
from amp.services.base import ServiceBuilder


class PropellerClient(APIResource):
    def __init__(self):
        config = Configuration("https://ssp-api.propellerads.com/v5", auth_handler=False, handler=None, service_name='Exchange Rate Service(AMP)')
        super().__init__(config)

    def get_adv_statistics(self):
        querystring = '/adv/statistics'
        return self.get(params = querystring)



