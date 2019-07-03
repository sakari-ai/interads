from flask_restful import Resource, reqparse

from controller.transformer import Transformer
from services.startapp_report import StartAppReportService
from services.zeropark import ZeroparkService


class InteradResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pid', type=str, required=False, help="only for Startapp") #only for startapp
    parser.add_argument('cid', type=str, required=True, help="cant be blank")
    parser.add_argument('token', type=str, required=True, help="cant be blank")
    parser.add_argument('startDate', type=str, required=True, help="cant be blank") #yyyymmdd for startapp, dd/mm/yyyy for zeropark
    parser.add_argument('endDate', type=str, required=True, help="cant be blank") #yyyymmdd for startapp, dd/mm/yyyy for zeropark

    @staticmethod
    def find_source(source, params):
        if source == "startapp":
            startapp = StartAppReportService(params['pid'], params["token"],
                                             params["startDate"], params["endDate"])
            return Transformer(params["cid"]).transform_startapp_data(startapp.get_report())
        elif source == "zeropark":
            zeropark = ZeroparkService(token=params["token"])
            return Transformer(params["cid"]).transform_zeropark_data(zeropark.get_all_campaigns_with_custom_interval(
                startDate=params["startDate"], endDate=params["endDate"]))

    def get(self, source):
        params = InteradResource.parser.parse_args()
        return self.find_source(source=source, params=params)




