from marshmallow import Schema,fields


class BodySchema(Schema):
    pid = fields.Str()
    cid = fields.Str()
    token = fields.Str()
    startDate = fields.Str()
    endDate = fields.Str()
