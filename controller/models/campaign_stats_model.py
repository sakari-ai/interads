from controller.schemas.campaign_stats_schema import CampaignStatsSchema
from controller.transformers.startapp_stats import StartappTransformer
from controller.transformers.zeropark_stats import ZeroparkTransformer
from core.exception.exceptions import WrongInputException
from services.startapp_report import StartAppReportService
from services.zeropark import ZeroparkService


class CampaignStatsModel(object):
    @classmethod
    def find_source(cls, source, params):
        if source == "startapp":
            try:
                startapp = StartAppReportService(params['pid'], params["token"],
                                                 params["startDate"], params["endDate"])
                model = StartappTransformer(params["cid"]).transform(startapp.get_report().data)
                schema = CampaignStatsSchema()
                return schema.dump(model)
            except WrongInputException as e:
                raise e
        elif source == "zeropark":
            try:
                zeropark = ZeroparkService(token=params["token"])
                model = ZeroparkTransformer(params["cid"]).transform(zeropark.get_all_campaigns_with_custom_interval(
                    startDate=params["startDate"], endDate=params["endDate"]).elements)
                schema = CampaignStatsSchema()
                return schema.dump(model)
            except WrongInputException as e:
                raise e
