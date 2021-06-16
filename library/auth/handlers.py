from itertools import chain
from typing import List, Optional

from jwt import ExpiredSignatureError, DecodeError
from sanic.request import Request

from config import settings

from .exceptions import AuthException, AuthExpiredException
from .jwt import get_token_info


def _find_request(args, kwargs) -> Optional[Request]:
    for item in chain(args, kwargs.values()):
        if isinstance(item, Request):
            return item

    return None


_user_field = 'user_id'
_auth_header = 'Authorization'
_auth_type = 'Bearer'


def require_auth(method):
    def decorator(optional=False, roles: List=...):
        def wrap(*args, **kwargs):
            request = _find_request(args, kwargs)

            if request is None and optional is False:
                raise AuthException

            auth = request.headers.get(_auth_header)
            auth_data = None
            if auth is not None:
                try:
                    auth_type, auth_data = auth.split(' ')  # Bearer <token>
                except IndexError:
                    pass
                else:
                    if auth_type != _auth_type:
                        auth_data = None

            if auth_data is None and optional is False:
                raise AuthException

            elif auth_data is None and optional is True:
                setattr(request.ctx, _user_field, None)
                return method(*args, **kwargs)

            try:
                jwt_data = get_token_info(auth_data, settings.JWT_SECRET)
            except ExpiredSignatureError:
                raise AuthExpiredException
            except DecodeError:
                raise AuthException

            setattr(request.ctx, _user_field, jwt_data.user_id)

            return method(*args, **kwargs)
        return wrap

    if callable(method):
        return decorator()

    else:
        return decorator
