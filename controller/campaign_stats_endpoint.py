from flask_restful import Resource
from flask import request
from marshmallow import ValidationError, EXCLUDE

from controller.models.campaign_stats_model import CampaignStatsModel
from controller.schemas.stats_auth_schema import StatsAuthSchema
from controller.schemas.stats_query_schema import StatsQuerySchema
from core.exception.exceptions import InputException


class CampaignStatsResource(Resource):
    def get(self, source):
        query = StatsQuerySchema(unknown=EXCLUDE)
        auth = StatsAuthSchema(unknown=EXCLUDE)
        try:
            queries = query.load(request.get_json())
            authentication = auth.load(request.get_json())

        except ValidationError as error:
            return error.messages, 400
        try:
            return CampaignStatsModel.find_source(source=source, query=queries, auth=authentication)
        except InputException as e:
            return e.messages, 400



