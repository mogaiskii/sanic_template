from marshmallow import fields

from api.users.base import ResponseUser
from library.api import RequestSchema, ResponseSchema


class RequestAuth(RequestSchema):
    login = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)


class ResponseTokens(ResponseSchema):
    auth_token = fields.String()
    refresh_token = fields.String()
    expire_at = fields.DateTime()


class ResponseAuth(ResponseSchema):
    user = fields.Nested(ResponseUser)
    tokens = fields.Nested(ResponseTokens)
