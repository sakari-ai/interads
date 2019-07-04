from marshmallow import Schema, fields


class InputRequirement(Schema):
    pid = fields.Str()
    cid = fields.Str(required=True)
    token = fields.Str(required=True)
    startDate = fields.Str(required=True)  # yyyymmdd for startapp, dd/mm/yyyy for zeropark
    endDate = fields.Str(required=True)  # yyyymmdd for startapp, dd/mm/yyyy for zeropark
