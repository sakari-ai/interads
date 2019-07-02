from core.delegation.responsehandler import ResponseHandler
from core.resource import APIResource, Configuration
from services.responses.startapp_optimization_response import StartAppOptimizationObject


class StartAppOptimizationService(APIResource):
    def __init__(self, pid, token):
        self._pid = pid
        self._token = token
        self.extend = {"partner": pid, "token": token}
        config = Configuration("https://api.startapp.com/adv/campaignOptimization/1.0",
                               auth_handler=False, handler=StartAppOptimizationHandler(),
                               service_name='Startapp Optimization Service(AMP)')
        super().__init__(config)

    def update_campaign_targeting(self, campaignid, dimensioneventids, dimension, include):
        """

        :param campaignid: list of strings
        :param dimensioneventids: list of strings
        :param dimension: list of strings
        :param include: bool
        :return:
        """

        body = {'campaignId': campaignid, 'dimensionEventIds': dimensioneventids,
                'dimension': dimension, 'include': include}

        return self.update("/blacklist", headers={'Content-Type': 'application/json'},
                           params=self.extend, json=body)

    def update_campaign_optimization(self, campaignid, optimization):
        """

        :param campaignid: list of strings
        :param optimization: list of list of list!
        :return:
        """

        body = {'campaignId': campaignid, 'optimization': optimization}

        return self.update("/optimize", headers={'Content-Type': 'application/json'},
                           params=self.extend, json=body)

    def get_campaign_optimization(self, campaignid, dimensions, startDate=None, endDate=None, limit=None, orderBy=None,
                                  getSummary=None):
        """

        :param campaignid: list of string
        :param dimensions: string
        :param startDate: date
        :param endDate: date
        :param limit: number
        :param orderBy: string
        :param getSummary: bool
        :return:
        """

        body = {'campaignId': campaignid, 'dimensions': dimensions}
        if startDate:
            body.update({'startDate': startDate})
        if endDate:
            body.update({'startDate': endDate})
        if limit:
            body.update({'startDate': limit})
        if orderBy:
            body.update({'startDate': orderBy})
        if getSummary:
            body.update({'startDate': getSummary})

        return self.create("/optimize", headers={'Content-Type': 'application/json'},
                           params=self.extend, json=body)


class StartAppOptimizationHandler(ResponseHandler):
    @staticmethod
    def handle(result):
        print(result.request.url)
        res = result.json()
        if "data" in res:
            return StartAppOptimizationObject(res)
        if res['success']:
            return "SUCCEEDED!"
        return "FAILED"






