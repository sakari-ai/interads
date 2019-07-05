from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from controller.models.campaign_stats_model import CampaignStatsModel
from controller.schemas.stats_input import StatsInput
from core.exception.exceptions import WrongInputException


class CampaignStatsResource(Resource):
    def get(self, source):
        body = StatsInput()
        try:
            params = body.load(request.get_json())
        except ValidationError as error:
            return error.messages, 400
        try:
            return CampaignStatsModel.find_source(source=source, params=params)
        except WrongInputException as e:
            return e.messages, 400



