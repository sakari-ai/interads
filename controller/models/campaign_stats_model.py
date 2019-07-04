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
            return StartappTransformer(params["cid"]).transform(startapp.get_report())
        elif source == "zeropark":
            zeropark = ZeroparkService(token=params["token"])
            return ZeroparkTransformer(params["cid"]).transform(zeropark.get_all_campaigns_with_custom_interval(
                startDate=params["startDate"], endDate=params["endDate"]))