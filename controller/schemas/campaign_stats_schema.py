from marshmallow import Schema, fields


class CampaignStatsSchema(Schema):
    impressions = fields.Int()
    clicks = fields.Int()
    spent = fields.Float()
