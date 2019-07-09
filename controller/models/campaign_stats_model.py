from controller.schemas.campaign_stats_schema import CampaignStatsSchema
from controller.transformers.startapp_stats import StartappTransformer
from controller.transformers.zeropark_stats import ZeroparkTransformer
from core.exception.exceptions import InputException
from services.startapp_report import StartAppReportService
from services.zeropark import ZeroparkService


class CampaignStatsModel(object):
    @classmethod
    def find_source(cls, source, query, auth):
        if source == "startapp":
            try:
                startapp = StartAppReportService(auth['partner_id'], auth["token"],
                                                 query["startDate"], query["endDate"])
                model = StartappTransformer(query["campaign_id"]).transform(startapp.get_report().data)
                schema = CampaignStatsSchema()
                return schema.dump(model)
            except InputException as e:
                raise e
        elif source == "zeropark":
            try:
                zeropark = ZeroparkService(token=auth["token"])
                model = ZeroparkTransformer(query["campaign_id"]).transform(zeropark.get_all_campaigns_with_custom_interval(
                    startDate=query["startDate"], endDate=query["endDate"]).elements)
                schema = CampaignStatsSchema()
                return schema.dump(model)
            except InputException as e:
                raise e
