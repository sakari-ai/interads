from controller.schemas.campaign_stats_schema import CampaignStatsSchema
from controller.transformers.startapp_stats import StartappTransformer
from controller.transformers.zeropark_stats import ZeroparkTransformer
from services.startapp_report import StartAppReportService
from services.zeropark import ZeroparkService


class CampaignStatsModel(object):
    @classmethod
    def find_source(cls, source, params):
        if source == "startapp":
            startapp = StartAppReportService(params['pid'], params["token"],
                                             params["startDate"], params["endDate"])
            model = StartappTransformer(params["cid"]).transform(startapp.get_report())
            schema = CampaignStatsSchema()
            if schema.dump(model):
                return schema.dump(model)
            return model
        elif source == "zeropark":
            zeropark = ZeroparkService(token=params["token"])
            model = ZeroparkTransformer(params["cid"]).transform(zeropark.get_all_campaigns_with_custom_interval(
                startDate=params["startDate"], endDate=params["endDate"]))
            schema = CampaignStatsSchema()
            if schema.dump(model):
                return schema.dump(model)
            return model
