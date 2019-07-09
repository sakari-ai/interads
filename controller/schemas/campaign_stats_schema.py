from marshmallow import Schema, fields


class CampaignStatsSchema(Schema):
    impressions = fields.Int(required=True)
    clicks = fields.Int(required=True)
    spent = fields.Float(required=True)
