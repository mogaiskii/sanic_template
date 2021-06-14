from marshmallow import fields, Schema

from api.users.base import ResponseUser


class ResponseUsers(Schema):
    users = fields.List(fields.Nested(ResponseUser))
