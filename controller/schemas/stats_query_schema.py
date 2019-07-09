from marshmallow import Schema, fields


class StatsQuerySchema(Schema):
    campaign_id = fields.Str(required=True)
    startDate = fields.Str(required=True)  # yyyymmdd for startapp, dd/mm/yyyy for zeropark
    endDate = fields.Str(required=True)  # yyyymmdd for startapp, dd/mm/yyyy for zeropark
