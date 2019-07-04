from controller.representatives.campaign_stats_object import CampaignStatsObject
from controller.schemas.campaign_stats_schema import CampaignStatsSchema


class StartappTransformer:
    def __init__(self, cid):
        self._cid = cid

    def transform(self, service):
        for i in service.data:
            if i['campaignId'] == self._cid:
                schema = CampaignStatsSchema()
                data = {'impressions': i["impressions"], "clicks": i["clicks"], "spent": i["spent"]}
                return CampaignStatsObject(**schema.load(data))

