from marshmallow import fields, Schema

from api.users.base import ResponseUser
from library.api import RequestSchema


class RequestAuth(RequestSchema):
    login = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)


class ResponseTokens(Schema):
    auth_token = fields.String()
    refresh_token = fields.String()
    expire_at = fields.DateTime()


class ResponseAuth(Schema):
    user = fields.Nested(ResponseUser)
    tokens = fields.Nested(ResponseTokens)
