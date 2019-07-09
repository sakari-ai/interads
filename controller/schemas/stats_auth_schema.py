from marshmallow import Schema, fields


class StatsAuthSchema(Schema):
    partner_id = fields.Str()
    token = fields.Str(required=True)
