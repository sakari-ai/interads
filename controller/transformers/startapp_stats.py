from controller.representatives.campaign_stats_object import CampaignStatsObject
from controller.schemas.campaign_stats_schema import CampaignStatsSchema
from core.exception.exceptions import WrongInputException


class StartappTransformer:
    def __init__(self, cid):
        self._cid = cid

    def transform(self, data):
        for i in data:
            if i['campaignId'] == self._cid:
                schema = CampaignStatsSchema()
                rdata = {'impressions': i["impressions"], "clicks": i["clicks"], "spent": i["spent"]}
                return CampaignStatsObject(**schema.load(rdata))
        raise WrongInputException("Your campaignId does not exist")

