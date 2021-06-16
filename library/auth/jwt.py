import datetime
from collections import namedtuple

import jwt
from marshmallow import fields, ValidationError

from library.api import ResponseSchema, RequestSchema

from .exceptions import AuthException


class JWTData(RequestSchema, ResponseSchema):
    user_id = fields.Integer(required=True, allow_none=False)
    exp = fields.Integer()


TokensPair = namedtuple('TokensPair', ['auth_token', 'refresh_token'])


_algorithm = "HS256"


def generate_user_tokens(user_id, jwt_secret, token_expiration, refresh_expiration) -> TokensPair:
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    exp = int((now + datetime.timedelta(seconds=token_expiration)).timestamp())
    data = JWTData().dump_from(user_id=user_id, exp=exp)
    auth_token = jwt.encode(data, jwt_secret, algorithm=_algorithm)

    refresh_exp = int((now + datetime.timedelta(seconds=refresh_expiration)).timestamp())
    refresh_data = JWTData().dump_from(user_id=user_id, exp=refresh_exp)
    refresh_token = jwt.encode(refresh_data, jwt_secret, algorithm=_algorithm)

    return TokensPair(auth_token, refresh_token)


def get_token_info(jwt_token, jwt_secret) -> JWTData:
    data = jwt.decode(jwt_token, jwt_secret, algorithms=[_algorithm])

    try:
        return JWTData().get_object(data)
    except ValidationError:
        raise AuthException
