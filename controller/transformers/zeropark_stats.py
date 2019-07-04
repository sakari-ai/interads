from controller.representatives.campaign_stats_object import CampaignStatsObject
from controller.schemas.campaign_stats_schema import CampaignStatsSchema


class ZeroparkTransformer:
    def __init__(self, cid):
        self._cid = cid

    def transform(self, service):
        for i in service.elements:
            if i['details']['id'] == self._cid:
                schema = CampaignStatsSchema()
                data = {'impressions': 0, "clicks": 0, "spent": i['stats']["spent"]}
                return CampaignStatsObject(**schema.load(data))
