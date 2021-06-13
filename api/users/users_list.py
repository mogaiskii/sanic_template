from marshmallow import fields, Schema


class ResponseUser(Schema):
    id = fields.Integer()
    login = fields.String()


class ResponseUsers(Schema):
    users = fields.List(fields.Nested(ResponseUser))
