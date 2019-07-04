from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from controller.models.campaign_stats_model import CampaignStatsModel
from controller.schemas.body_schema import BodySchema
from controller.schemas.campaign_stats_schema import CampaignStatsSchema


class CampaignStatsResource(Resource):
    def get(self, source):
        body = BodySchema()
        try:
            params = body.load(request.get_json())
        except ValidationError as error:
            return error.messages, 400
        model = CampaignStatsModel.find_source(source=source, params=params)
        schema = CampaignStatsSchema()
        return schema.dump(model)


