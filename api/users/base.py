from marshmallow import fields, Schema


class ResponseUser(Schema):
    id = fields.Integer()
    login = fields.String()

